options(digits=6)
# Independent NB2 counts, same generation as the primer; disjoint random holdout.
set.seed(46705); n<-400; x<-runif(n,-1,1); effort<-runif(n,.5,2); y<-rnbinom(n,mu=effort*exp(.4+.7*x),size=2); d<-data.frame(y,x,effort)
set.seed(45); test<-sample(n,100); tr<-d[-test,]; te<-d[test,]
p<-glm(y~x+offset(log(effort)),poisson,data=tr); nb<-MASS::glm.nb(y~x+offset(log(effort)),data=tr)
mp<-predict(p,te,type='response'); mn<-predict(nb,te,type='response'); threshold<-5
set.seed(991); sim<-function(kind) replicate(3000,{v<-if(kind=='p') rpois(nrow(te),mp) else rnbinom(nrow(te),mu=mn,size=nb$theta); c(zeros=sum(v==0),tail=sum(v>=threshold))})
a<-sim('p'); b<-sim('n'); cat('NB observed zeros/tail',sum(te$y==0),sum(te$y>=threshold),'\n'); print(rbind(Poisson=apply(a,1,quantile,c(.025,.5,.975)),NB=apply(b,1,quantile,c(.025,.5,.975))))
cat('NB test log scores',mean(dpois(te$y,mp,log=TRUE)),mean(dnbinom(te$y,mu=mn,size=nb$theta,log=TRUE)),'shape',nb$theta,'\n')
stopifnot(nb$converged,is.finite(nb$theta),mean(dnbinom(te$y,mu=mn,size=nb$theta,log=TRUE))>mean(dpois(te$y,mp,log=TRUE)))
# Existing eight-site GLMM, fit by numerical integration; hold sites 7-8 out.
set.seed(467); x<-rep(seq(-1.5,1.5,length.out=12),8); group<-rep(1:8,each=12); latent<-rep(c(-.7,-.5,-.3,-.1,.1,.3,.5,.7),each=12); y<-rpois(length(x),exp(.45+.35*x+latent))
llsite<-function(par,k,tol=1e-8) {idx<-group==k; sig<-exp(par[3]); li<-function(v)sum(dpois(y[idx],exp(par[1]+par[2]*x[idx]+v),log=TRUE))+dnorm(v,0,sig,log=TRUE); mode<-optimize(function(v)-li(v),c(-10*sig,10*sig))$minimum; sc<-li(mode); sc+log(integrate(function(v)exp(vapply(v,li,numeric(1))-sc),-Inf,Inf,rel.tol=tol)$value)}
fitg<-function(ids){p<-glm(y[group%in%ids]~x[group%in%ids],poisson); optim(c(coef(p),log(.4)),function(par)-sum(vapply(ids,function(k)llsite(par,k),numeric(1))),method='BFGS',control=list(maxit=300,reltol=1e-9))}
f<-fitg(1:8); h<-fitg(1:6); stopifnot(f$convergence==0,h$convergence==0)
# Conditional distribution for site 1, given its observations and fixed fitted parameters.
par<-f$par; sig<-exp(par[3]); idx<-group==1; lp<-function(v)sum(dpois(y[idx],exp(par[1]+par[2]*x[idx]+v),log=TRUE))+dnorm(v,0,sig,log=TRUE); mode<-optimize(function(v)-lp(v),c(-5,5))$minimum; grid<-seq(-4,4,length.out=16001); w<-exp(vapply(grid,lp,numeric(1))-lp(mode)); w<-w/sum(w); qgrid<-function(p)grid[which(cumsum(w)>=p)[1]]
set.seed(123); b1<-sample(grid,100000,replace=TRUE,prob=w); knownmu<-exp(par[1]+b1); knowny<-rpois(length(b1),knownmu); newy<-rpois(100000,exp(par[1]+rnorm(100000,0,sig))); cat('GLMM site1 b mode/mean/interval',mode,sum(grid*w),qgrid(.025),qgrid(.975),'\n'); cat('GLMM x0 conditional mean, future count interval',mean(knownmu),quantile(knowny,c(.025,.975)),'new mean, interval',exp(par[1]+sig^2/2),quantile(newy,c(.025,.975)),'\n')
# Held-out groups: score full group joint density; compare independent Poisson, whose conditional mean is correctly fitted marginally here.
gd<-data.frame(y=y,x=x,group=group); pp<-glm(y~x,poisson,data=gd[gd$group<=6,]); base<-sum(dpois(gd$y[gd$group>6],predict(pp,newdata=gd[gd$group>6,],type='response'),log=TRUE)); mixed<-sum(vapply(7:8,function(k)llsite(h$par,k),numeric(1))); cat('GLMM held-group joint log scores Poisson/mixed',base,mixed,'sigma',exp(h$par[3]),'\n')
stopifnot(abs(sum(w)-1)<1e-10,all(is.finite(c(base,mixed))))
# Near duplicate gradients: held-out blocks in independent synthetic rows.
set.seed(46710); N<-500; x<-runif(N,-2,2); w<-x+rnorm(N,0,.04); block<-sample(rep(1:5,length.out=N)); y<-rpois(N,exp(.5+.35*x+.45*sin(2*x))); d<-data.frame(x,w,block,y); tr<-d[d$block!=5,]; te<-d[d$block==5,]
two<-mgcv::gam(y~s(x,k=8)+s(w,k=8),family=poisson,method='REML',data=tr); one<-mgcv::gam(y~s(x,k=8),family=poisson,method='REML',data=tr); conc<-mgcv::concurvity(two,full=TRUE); pred1<-predict(one,te,type='response'); pred2<-predict(two,te,type='response'); cat('GAM concurvity estimate x/w',conc['estimate','s(x)'],conc['estimate','s(w)'],'\n'); cat('GAM heldout logscore one/two',mean(dpois(te$y,pred1,log=TRUE)),mean(dpois(te$y,pred2,log=TRUE)),'mean abs prediction diff',mean(abs(pred1-pred2)),'\n'); stopifnot(conc['estimate','s(x)']>.9,all(is.finite(pred1)),all(is.finite(pred2)))
# Intercept-only zero inflation/hurdle, independently held out from existing sample.
set.seed(468); raw<-rpois(300,2); z<-ifelse(runif(300)<.3,0,raw); set.seed(46); ti<-sample(300,100); train<-z[-ti]; test<-z[ti]
zobj<-function(p){pi<-plogis(p[1]); mu<-exp(p[2]); -sum(ifelse(train==0,log(pi+(1-pi)*exp(-mu)),log1p(-pi)+dpois(train,mu,log=TRUE)))}
hobj<-function(p){q<-plogis(p[1]); mu<-exp(p[2]); -sum(ifelse(train==0,log(q),log1p(-q)+dpois(train,mu,log=TRUE)-log1p(-exp(-mu))))}
zi<-optim(c(-1,.5),zobj,method='BFGS'); hu<-optim(c(-1,.5),hobj,method='BFGS'); stopifnot(zi$convergence==0,hu$convergence==0)
pi<-plogis(zi$par[1]); mu<-exp(zi$par[2]); q<-plogis(hu$par[1]); hm<-exp(hu$par[2]); pm<-mean(train)
set.seed(998); B<-3000; draw<-function(kind){if(kind=='pois') return(rpois(100,pm)); if(kind=='zi') return(ifelse(runif(100)<pi,0,rpois(100,mu))); positive<-qpois(runif(100,min=exp(-hm),max=1),hm); ifelse(runif(100)<q,0,positive)}
summ<-function(v)c(zeros=sum(v==0),tail=sum(v>=5),mean=mean(v)); cat('ZERO observed',summ(test),'\n'); for(k in c('pois','zi','hurdle')){v<-replicate(B,summ(draw(k))); cat('ZERO',k,'\n'); print(t(apply(v,1,quantile,c(.025,.5,.975))))}
lzip<-ifelse(test==0,log(pi+(1-pi)*exp(-mu)),log1p(-pi)+dpois(test,mu,log=TRUE)); lh<-ifelse(test==0,log(q),log1p(-q)+dpois(test,hm,log=TRUE)-log1p(-exp(-hm))); cat('ZERO test log scores',mean(dpois(test,pm,log=TRUE)),mean(lzip),mean(lh),'\n'); stopifnot(max(abs(lzip-lh))<.001)
# Analytic Poisson rate and independent-site rate heterogeneity failure.
counts<-c(0,0,0,0,0,0,0,3,4,5,7,9); N<-length(counts); S<-sum(counts); a<-2; rate<-1; A<-a+S; R<-rate+N
cat('BAYES posterior shape rate mean interval',A,R,A/R,qgamma(c(.025,.975),A,rate=R),'future interval',qnbinom(c(.025,.975),size=A,prob=R/(R+1)),'MLE',mean(counts),'sensitivity mean', (10+S)/(5+N),'\n')
# Prior and posterior predictive replicated totals and zero frequencies, with fitted-rate uncertainty.
set.seed(700); repcheck<-function(shape,rate,B=30000){lambda<-rgamma(B,shape,rate=rate); yy<-matrix(rpois(B*N,rep(lambda,each=N)),nrow=N); cbind(total=colSums(yy),zeros=colSums(yy==0),tail=colSums(yy>=5))}; prior_tight<-repcheck(2,10); prior<-repcheck(a,rate); post<-repcheck(A,R); cat('BAYES observed total zeros tail',S,sum(counts==0),sum(counts>=5),'\n'); cat('BAYES prior/post predictive ranges\n'); print(rbind(tight_prior=apply(prior_tight,2,quantile,c(.025,.5,.975)),prior=apply(prior,2,quantile,c(.025,.5,.975)),post=apply(post,2,quantile,c(.025,.5,.975))))
# Repair assumption: independent Gamma random rates with fixed shape 1; numerical posterior for common mean lambda, same Gamma prior.
logpost<-function(lam) sum(dnbinom(counts,mu=lam,size=1,log=TRUE))+dgamma(lam,a,rate=rate,log=TRUE); grid<-seq(.001,12,length.out=24000); lw<-vapply(grid,logpost,numeric(1)); ww<-exp(lw-max(lw)); ww<-ww/sum(ww); set.seed(701); lam<-sample(grid,30000,replace=TRUE,prob=ww); yy<-matrix(rnbinom(N*length(lam),mu=rep(lam,each=N),size=1),nrow=N); repair<-cbind(total=colSums(yy),zeros=colSums(yy==0),tail=colSums(yy>=5)); cat('BAYES repair posterior mean',sum(grid*ww),'predictive ranges\n'); print(apply(repair,2,quantile,c(.025,.5,.975))); stopifnot(abs(sum(ww)-1)<1e-10,abs(sum(dnbinom(0:500,size=A,prob=R/(R+1)))-1)<1e-8)
wide<-seq(.001,20,by=.0005); wl<-vapply(wide,logpost,numeric(1)); ww2<-exp(wl-max(wl)); ww2<-ww2/sum(ww2); difference<-abs(sum(grid*ww)-sum(wide*ww2)); cat('BAYES grid wide mean/difference',sum(wide*ww2),difference,'mass above 11',sum(ww2[wide>11]),'\n'); stopifnot(difference<1e-4,sum(ww2[wide>11])<1e-5)
