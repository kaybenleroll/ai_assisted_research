# R01/R03/R04: independent teaching calculations, fixed inputs; no checkout writes.
options(digits=10, width=150)
# Same 342 penguins as the existing real example; species-only model is descriptive.
p<-read.csv('data/penguins.csv',na.strings='NA')
p$species<-factor(p$species,levels=c('Adelie','Chinstrap','Gentoo'))
d<-p[complete.cases(p[c('body_mass_g','species')]),]
stopifnot(nrow(d)==342)
g<-lm(body_mass_g~species,data=d)
new<-data.frame(species=factor('Adelie',levels=levels(d$species)))
ci<-predict(g,new,interval='confidence',level=.95)
pi<-predict(g,new,interval='prediction',level=.95)
cat('penguin mean interval',ci,'future interval',pi,'residual df',df.residual(g),'\n')
stopifnot(pi[1,'lwr']<ci[1,'lwr'],pi[1,'upr']>ci[1,'upr'])
# Gaussian likelihood ratio compares ML variance separately under both models.
g0<-lm(body_mass_g~1,data=d); llr<-2*as.numeric(logLik(g)-logLik(g0)); df<-attr(logLik(g),'df')-attr(logLik(g0),'df'); pval<-pchisq(llr,df,lower.tail=FALSE)
cat('penguin nested LR',llr,'df',df,'p',pval,'n same',nobs(g),nobs(g0),'\n')
stopifnot(nobs(g)==nobs(g0),df==2,llr>0,pval<.01)
# Four grouped binomial observations, known trial counts. The interaction is real on link and response scales.
id<-expand.grid(x=c(0,1),habitat=c(0,1)); id$success<-c(20,40,55,85); id$failure<-100-id$success
mi<-glm(cbind(success,failure)~x*habitat,family=binomial,data=id)
V<-vcov(mi); b<-coef(mi)
eta<-predict(mi,id,type='link'); pp<-predict(mi,id,type='response')
# expand.grid: h0x0, h0x1, h1x0, h1x1.
diff0<-pp[3]-pp[1];diff1<-pp[4]-pp[2]; did<-diff1-diff0
vh<-V['habitat','habitat']; vint<-V['x:habitat','x:habitat']; covhi<-V['habitat','x:habitat']; varcontrast<-vh+vint+2*covhi
cat('interaction coefficients',b,'cov(h,interaction)',covhi,'logodds habitat x0',b['habitat'],'x1',b['habitat']+b['x:habitat'],'variance at x1',varcontrast,'naive ignoring covariance',vh+vint,'probabilities',pp,'habitat contrasts',diff0,diff1,'difference in differences',did,'\n')
stopifnot(max(abs(pp-c(.2,.4,.55,.85)))<1e-8,abs(covhi)>1e-4,varcontrast>0)
# Complete separation: x=1 all successes; same two-group synthetic data as hand IRLS discussion.
x<-c(rep(0,10),rep(1,10)); y<-c(0,0,0,0,0,0,1,1,1,1,rep(1,10)); X<-cbind(1,x)
# Fit for finite iteration limits to expose drift; no claim of finite MLE.
fit15<-suppressWarnings(glm(y~x,family=binomial(),control=glm.control(maxit=15)))
fit25<-suppressWarnings(glm(y~x,family=binomial(),control=glm.control(maxit=25)))
penfit<-function(lambda){f<-function(b){eta<-drop(X%*%b); sum(log1p(exp(eta))-y*eta)+lambda*sum(b*b)/2};optim(c(0,0),f,method='BFGS',control=list(reltol=1e-12))}
fits<-lapply(c(.25,1,4),penfit)
cat('separated unpenalised coef iter15',coef(fit15),'iter25',coef(fit25),'fitted probabilities',predict(fit25,newdata=data.frame(x=c(0,1)),type='response'),'\n')
for(i in 1:3)cat('penalty',c(.25,1,4)[i],'coef',fits[[i]]$par,'probabilities',plogis(c(fits[[i]]$par[1],sum(fits[[i]]$par))),'objective convergence',fits[[i]]$convergence,'\n')
stopifnot(coef(fit25)[2]>coef(fit15)[2]+2,all(vapply(fits,function(o)o$convergence==0,logical(1))))
# Gamma simulation: known log-linear mean, shape 4; fixed train/test split.
set.seed(222468); n<-400; x<-runif(n,-1,1); true_mu<-exp(1+1.1*x); y<-rgamma(n,shape=4,scale=true_mu/4)
train<-data.frame(x=x[1:250],y=y[1:250]); test<-data.frame(x=x[251:n],y=y[251:n])
m0<-glm(y~1,family=Gamma(link='log'),data=train)
m1<-glm(y~x,family=Gamma(link='log'),data=train)
stopifnot(m0$converged,m1$converged)
score<-function(m){mu<-predict(m,newdata=test,type='response'); shape<-1/summary(m)$dispersion; lb<-qgamma(.025,shape=shape,scale=mu/shape);ub<-qgamma(.975,shape=shape,scale=mu/shape);c(neglog=-mean(dgamma(test$y,shape=shape,scale=mu/shape,log=TRUE)),coverage=mean(test$y>=lb & test$y<=ub), mae=mean(abs(test$y-mu)))}
groups<-function(m){mu<-predict(m,newdata=test,type='response');tapply(test$y-mu,test$x>0,mean)}
cat('gamma model0 coeff',coef(m0),'dispersion',summary(m0)$dispersion,'test negative log score,coverage,mae',score(m0),'residual mean by xnegative/xpositive',groups(m0),'\n')
cat('gamma model1 coeff',coef(m1),'dispersion',summary(m1)$dispersion,'test negative log score,coverage,mae',score(m1),'residual mean by xnegative/xpositive',groups(m1),'\n')
# Parametric bootstrap refits: regenerate training responses, re-estimate mean and dispersion,
# then generate a future observation at x=.8 for each fitted model.
set.seed(222469); B<-500; fitted_mu<-fitted(m1); shape<-1/summary(m1)$dispersion
future<-rep(NA_real_,B); means<-rep(NA_real_,B)
for(i in seq_len(B)){
 sim<-train; sim$y<-rgamma(nrow(sim),shape=shape,scale=fitted_mu/shape)
 ff<-glm(y~x,family=Gamma(link='log'),data=sim)
 if(ff$converged){means[i]<-predict(ff,newdata=data.frame(x=.8),type='response');sh<-1/summary(ff)$dispersion;future[i]<-rgamma(1,shape=sh,scale=means[i]/sh)}
}
failed<-sum(is.na(future)); cat('gamma bootstrap failures',failed,'mean at x.8',predict(m1,newdata=data.frame(x=.8),type='response'),'mean parameter bootstrap interval',quantile(means,c(.025,.975),na.rm=TRUE),'future observation bootstrap interval',quantile(future,c(.025,.975),na.rm=TRUE),'\n')
stopifnot(failed==0,score(m1)['neglog']<score(m0)['neglog'],all(is.finite(future)),diff(quantile(future,c(.025,.975)))>diff(quantile(means,c(.025,.975))))
