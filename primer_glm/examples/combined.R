# Known-truth simulation; all choices below precede the held-out evaluation.
library(mgcv)
options(digits=10, width=160)
set.seed(4682026)
ns <- 72; nv <- 4
d <- data.frame(site=factor(rep(seq_len(ns), each=nv)), x=runif(ns*nv,-1,1), effort=runif(ns*nv,0.6,1.6))
b <- rnorm(ns,0,0.55)
d$y <- rnbinom(nrow(d), mu=d$effort*exp(0.6+0.75*sin(pi*d$x)+b[as.integer(d$site)]), size=2)
train <- droplevels(subset(d,as.integer(site)<=54))
test <- subset(d,as.integer(site)>54)
stopifnot(nrow(train)==216,nrow(test)==72,!any(levels(train$site) %in% as.character(test$site)),all(d$effort>0))
# Candidate specifications are fixed before examining test scores.
models <- list(
 poisson=gam(y~x+offset(log(effort)),data=train,family=poisson(),method='REML'),
 nb=gam(y~x+offset(log(effort)),data=train,family=nb(),method='REML'),
 nb_site=gam(y~x+s(site,bs='re')+offset(log(effort)),data=train,family=nb(),method='REML'),
 nb_smooth=gam(y~s(x,k=7)+offset(log(effort)),data=train,family=nb(),method='REML'),
 combined=gam(y~s(x,k=7)+s(site,bs='re')+offset(log(effort)),data=train,family=nb(),method='REML'))
stopifnot(all(vapply(models,function(m) isTRUE(m$converged),logical(1))))
# Midpoint quadrature in standard-normal units. Log-sum-exp stabilises a joint site likelihood.
score <- function(y,eta,theta,sigma,n=1600L,limit=9) {
 if(sigma==0) return(sum(if(is.infinite(theta)) dpois(y,exp(eta),log=TRUE) else dnbinom(y,mu=exp(eta),size=theta,log=TRUE)))
 z <- -limit+(seq_len(n)-.5)*2*limit/n
 ll <- vapply(z,function(t) sum(dnbinom(y,mu=exp(eta+sigma*t),size=theta,log=TRUE)),numeric(1)) + dnorm(z,log=TRUE)
 a <- max(ll); a+log(sum(exp(ll-a))*2*limit/n)
}
# Integrate a future count CDF over the new site's normal intercept.
future_cdf <- function(q, eta, theta, sigma, n, limit) {
 z <- -limit+(seq_len(n)-.5)*2*limit/n
 weights <- dnorm(z)*2*limit/n
 mu <- exp(eta+sigma*z)
 vapply(q,function(k) sum(weights*pnbinom(k,size=theta,mu=mu)),numeric(1))
}
get_sigma <- function(m) {
 if(!any(vapply(m$smooth,function(s) identical(s$label,'s(site)'),logical(1)))) return(0)
 v <- gam.vcomp(m,rescale=TRUE); vc <- if(is.list(v)) v$vc else v; if(is.null(dim(vc))) unname(vc['s(site)']) else unname(vc['s(site)','std.dev'])
}
rows <- list(); fixtures <- list()
for(nm in names(models)) {
 m<-models[[nm]]; sig<-get_sigma(m); theta<-if(nm=='poisson') Inf else m$family$getTheta(TRUE)
 # Excluding the random term gives b=0, not integration over a new site.
 pred_data <- test
 if(sig>0) pred_data$site <- factor(rep(levels(train$site)[1],nrow(test)),levels=levels(train$site))
 eta<-as.numeric(predict(m,newdata=pred_data,type='link',exclude=if(sig>0) 's(site)' else NULL))
 g<-split(seq_len(nrow(test)),test$site,drop=TRUE)
 lo<-vapply(g,function(i) score(test$y[i],eta[i],theta,sig,1600L),numeric(1))
 hi<-vapply(g,function(i) score(test$y[i],eta[i],theta,sig,3200L),numeric(1))
 wider<-vapply(g,function(i) score(test$y[i],eta[i],theta,sig,3200L,10),numeric(1))
 stopifnot(max(abs(lo-hi))<1e-7,max(abs(hi-wider))<1e-7,all(is.finite(hi)),sig>=0,theta>0)
 rows[[nm]]<-data.frame(model=nm,theta=theta,sigma=sig,edf=sum(m$edf),joint_log_score=sum(hi))
 if(nm=='combined') {
   i<-g[[1]]; expected<-score(test$y[i],eta[i],theta,sig,3200L)
   cdf <- future_cdf(0:80,eta[i[1]],theta,sig,3200L,9)
 cdf_coarse <- future_cdf(0:80,eta[i[1]],theta,sig,1600L,9)
 cdf_wide <- future_cdf(0:80,eta[i[1]],theta,sig,3200L,10)
 stopifnot(max(abs(cdf-cdf_coarse))<1e-7,max(abs(cdf-cdf_wide))<1e-7, 1-tail(cdf,1)<1e-10,all(diff(cdf)>=0))
 # Discrete equal-tail quantiles: min integer k for which F(k) >= p.
 interval <- vapply(c(.025,.975),function(p) which(cdf>=p)[1]-1L,integer(1))
 cat('Future count equal-tail 95% interval:',interval,'; F(0), F(upper-1), F(upper), tail beyond 80:',cdf[1],cdf[interval[2]],cdf[interval[2]+1],1-tail(cdf,1),'\n')
 fixtures[[1]]<-data.frame(y=test$y[i],eta=eta[i],theta=theta,sigma=sig, conditional_b=0.25,
      conditional_mean=exp(eta[i]+0.25), integrated_mean=exp(eta[i]+sig^2/2), joint_log_score=expected, predictive_lower=interval[1], predictive_upper=interval[2], predictive_cdf_upper=cdf[interval[2]+1])
   cat('Combined first held-out site; b=0 / b=.25 / integrated means, observations:\n')
   print(data.frame(y=test$y[i],b0=exp(eta[i]),conditional=exp(eta[i]+.25),integrated=exp(eta[i]+sig^2/2)))
   cat('First site joint log predictive density:',expected,'; first visit predictive P(Y=0):',exp(score(0,eta[i[1]],theta,sig,3200L)),'\n')
   reference <- read.csv('examples/combined-fixture.csv')
   stopifnot(identical(as.integer(reference$y),as.integer(test$y[i])),max(abs(reference$eta-eta[i]))<1e-7,abs(reference$joint_log_score[1]-expected)<1e-7,identical(as.integer(reference[1,c('predictive_lower','predictive_upper')]),interval),abs(reference$predictive_cdf_upper[1]-cdf[interval[2]+1])<1e-7)
 }
}
results<-do.call(rbind,rows); print(results,row.names=FALSE)
cat('Training: 54 sites, 216 observations; test: 18 new sites, 72 observations. Test scores are sums of joint site log densities.\n')
write.csv(fixtures[[1]],file.path(Sys.getenv('EXAMPLE_OUT',tempdir()),'combined-fixture.csv'),row.names=FALSE,quote=FALSE)
