set.seed(467)
x <- rep(seq(-1.5,1.5,length.out=12),8); group <- rep(1:8,each=12)
b <- rep(c(-.7,-.5,-.3,-.1,.1,.3,.5,.7),each=12)
y <- rpois(length(x), exp(.45+.35*x+b))
d <- data.frame(x,group,y)
pois <- glm(y~x, family=poisson, data=d)
quasi <- glm(y~x, family=quasipoisson, data=d)
nb <- MASS::glm.nb(y~x,data=d)
cat('poisson_quasi_coef_maxdiff',max(abs(coef(pois)-coef(quasi))),'quasi_dispersion',summary(quasi)$dispersion,'nb_theta',nb$theta,'\n')
stopifnot(max(abs(coef(pois)-coef(quasi)))<1e-8, summary(quasi)$dispersion>0, nb$theta>0)
gam <- mgcv::gam(y~s(x,k=6),family=poisson,method='REML',data=d)
cat('gam_edf',sum(gam$edf),'prediction',predict(gam,newdata=data.frame(x=0),type='response'),'\n')
stopifnot(is.finite(gam$gcv.ubre))
# Marginal random-intercept Poisson likelihood via one-dimensional adaptive integration.
ll_group <- function(par, k, tolerance=1e-7) {
 idx <- group==k; sig <- exp(par[3])
 log_integrand <- function(v) sum(dpois(y[idx],exp(par[1]+par[2]*x[idx]+v),log=TRUE))+dnorm(v,0,sig,log=TRUE)
 mode <- optimize(function(v) -log_integrand(v),c(-10*sig,10*sig))$minimum
 scale <- log_integrand(mode)
 f <- function(u) exp(vapply(u,log_integrand,numeric(1))-scale)
 scale + log(integrate(f,-Inf,Inf,rel.tol=tolerance)$value)
}
obj <- function(par) -sum(vapply(1:8,function(k) ll_group(par,k),numeric(1)))
fit <- optim(c(coef(pois),log(.4)),obj,method='BFGS',control=list(maxit=300,reltol=1e-9))
cat('glmm_convergence',fit$convergence,'conditional_mu0',exp(fit$par[1]),'marginal_mu0',exp(fit$par[1]+exp(2*fit$par[3])/2),'sigma',exp(fit$par[3]),'\n')
stopifnot(fit$convergence==0,is.finite(fit$value))
coarse <- sum(vapply(1:8,function(k)ll_group(fit$par,k,1e-5),numeric(1)))
fine <- sum(vapply(1:8,function(k)ll_group(fit$par,k,1e-9),numeric(1)))
cat('glmm_quadrature_loglik_difference',abs(coarse-fine),'\n'); stopifnot(abs(coarse-fine)<1e-5)
# Intercept-only Poisson mixture/hurdle likelihoods, deliberately simple models.
set.seed(468); raw <- rpois(300,2); z <- ifelse(runif(300)<.3,0,raw)
zip_obj <- function(par) {pi<-plogis(par[1]); mu<-exp(par[2]); -sum(ifelse(z==0,log(pi+(1-pi)*exp(-mu)),log1p(-pi)+dpois(z,mu,log=TRUE)))}
hur_obj <- function(par) {q<-plogis(par[1]); mu<-exp(par[2]); -sum(ifelse(z==0,log(q),log1p(-q)+dpois(z,mu,log=TRUE)-log1p(-exp(-mu))))}
zip <- optim(c(-1,.5),zip_obj,method='BFGS'); hur <- optim(c(-1,.5),hur_obj,method='BFGS')
cat('zi_convergence',zip$convergence,'zero_prob',plogis(zip$par[1])+(1-plogis(zip$par[1]))*exp(-exp(zip$par[2])),'hurdle_convergence',hur$convergence,'zero_prob',plogis(hur$par[1]),'observed_zero',mean(z==0),'\n')
stopifnot(zip$convergence==0,hur$convergence==0)
zip_mean <- (1-plogis(zip$par[1]))*exp(zip$par[2]); hurdle_mean <- (1-plogis(hur$par[1]))*exp(hur$par[2])/(1-exp(-exp(hur$par[2])))
cat('zi_mean',zip_mean,'hurdle_mean',hurdle_mean,'observed_mean',mean(z),'\n'); stopifnot(zip_mean>0,hurdle_mean>0)
# Beta-binomial conjugate update, deterministic posterior numeric integration cross-check.
a<-2; bb<-2; successes<-7; trials<-10
postmean<-(a+successes)/(a+bb+trials)
intmean<-integrate(function(p) p*dbeta(p,a+successes,bb+trials-successes),0,1)$value
cat('bayes_posterior_mean',postmean,'quadrature_error',abs(postmean-intmean),'\n')
stopifnot(abs(postmean-intmean)<1e-9)
# Distinct categorical outcomes; probability output uses fixed new observations.
set.seed(469); N<-240; x2<-seq(-1.5,1.5,length.out=N); z2<-rlogis(N)+.7*x2
ord<-ordered(cut(z2,c(-Inf,-.7,.7,Inf),labels=c('low','medium','high')))
od<-data.frame(x=x2,ord=ord)
ordfit<-MASS::polr(ord~x,data=od,Hess=TRUE,method='logistic')
cat('ordinal_prob',paste(round(predict(ordfit,newdata=data.frame(x=0),type='probs'),6),collapse=' '),'\n')
stopifnot(abs(sum(predict(ordfit,newdata=data.frame(x=0),type='probs'))-1)<1e-8)
if (requireNamespace('nnet',quietly=TRUE)) {
 u<-runif(N); p1<-plogis(-.5+x2)*.55; p2<-plogis(.4-x2)*.55
 caty<-factor(ifelse(u<p1,'A',ifelse(u<p1+p2,'B','C')))
 mm<-nnet::multinom(caty~x2,trace=FALSE)
 pr<-predict(mm,newdata=data.frame(x2=0),type='probs')
 cat('multinomial_convergence',mm$convergence,'prob',paste(round(pr,6),collapse=' '),'\n')
 stopifnot(mm$convergence==0,abs(sum(pr)-1)<1e-8)
} else stop('nnet required for the multinomial example')
# Logistic GLM posterior by direct two-dimensional grid quadrature, normal priors.
xb<-c(-2,-1.5,-1,-.5,0,.5,1,1.5,2,2.5); yb<-c(0,1,0,0,1,0,1,1,0,1)
grid<-seq(-6,6,length.out=241); grid2<-expand.grid(intercept=grid,slope=grid)
logw<-vapply(seq_len(nrow(grid2)),function(i) {eta<-grid2$intercept[i]+grid2$slope[i]*xb; sum(dbinom(yb,1,plogis(eta),log=TRUE))+dnorm(grid2$intercept[i],0,2,log=TRUE)+dnorm(grid2$slope[i],0,2,log=TRUE)},numeric(1))
w<-exp(logw-max(logw)); w<-w/sum(w)
cat('bayes_logistic_predict_x1',sum(w*plogis(grid2$intercept+grid2$slope)),'boundary_mass',sum(w[abs(grid2$intercept)>5.5 | abs(grid2$slope)>5.5]),'\n')
stopifnot(sum(w[abs(grid2$intercept)>5.5 | abs(grid2$slope)>5.5])<.01)

# Check discretisation, not merely posterior boundary mass.
posterior_grid <- function(n) {
 grid<-seq(-6,6,length.out=n); a<-expand.grid(intercept=grid,slope=grid)
 lw<-vapply(seq_len(nrow(a)),function(i) {eta<-a$intercept[i]+a$slope[i]*xb; sum(dbinom(yb,1,plogis(eta),log=TRUE))+dnorm(a$intercept[i],0,2,log=TRUE)+dnorm(a$slope[i],0,2,log=TRUE)},numeric(1))
 w<-exp(lw-max(lw)); sum(w*plogis(a$intercept+a$slope))/sum(w)
}
p161<-posterior_grid(161); p321<-posterior_grid(321)
cat('bayes_grid_161',p161,'grid_321',p321,'difference',abs(p161-p321),'\n'); stopifnot(abs(p161-p321)<1e-4)
