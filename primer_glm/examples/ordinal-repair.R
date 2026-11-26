# Pre-specified counterexample: non-proportional cumulative logits, with a disjoint test set.
set.seed(472)
N<-3000; x<-runif(N,-1,1)
# Ordered cumulative logits are -1-.2*x and 1-1.1*x, for every x in [-1,1].
c1<-plogis(-1-.2*x); c2<-plogis(1-1.1*x)
stopifnot(all(c1<c2))
u<-runif(N); y<-ordered(ifelse(u<c1,'low',ifelse(u<c2,'middle','high')),levels=c('low','middle','high'))
d<-data.frame(x,y); train<-d[1:2000,]; test<-d[2001:3000,]
fit1<-glm(I(y=='low')~x,data=train,family=binomial())
fit2<-glm(I(y!='high')~x,data=train,family=binomial())
ord<-MASS::polr(y~x,data=train,method='logistic',Hess=TRUE)
mult<-nnet::multinom(y~x,data=train,trace=FALSE,maxit=300)
po<-predict(ord,newdata=test,type='probs'); pm<-predict(mult,newdata=test,type='probs')
truth<-model.matrix(~y-1,test); colnames(truth)<-levels(y)
# Evaluate held-out log loss and multicategory Brier score on exactly the same observations.
logloss<-function(p)-mean(log(p[cbind(seq_len(nrow(test)),as.integer(test$y))]))
brier<-function(p) mean(rowSums((p-truth)^2))
cat('fitted_cumulative_logit_slopes',coef(fit1)[2],coef(fit2)[2],'proportional_slope_sign_adjusted',-coef(ord)[1],'\n')
cat('heldout_logloss_proportional',logloss(po),'multinomial',logloss(pm),'heldout_brier_proportional',brier(po),'multinomial',brier(pm),'\n')
for(q in c(-.8,.8)) {
 new<-data.frame(x=q); tprob<-c(plogis(-1-.2*q),plogis(1-1.1*q)-plogis(-1-.2*q),1-plogis(1-1.1*q))
 cat('x',q,'true',tprob,'ordinal',predict(ord,newdata=new,type='probs'),'multinomial',predict(mult,newdata=new,type='probs'),'\n')
}
stopifnot(mult$convergence==0,all(abs(rowSums(po)-1)<1e-8),all(abs(rowSums(pm)-1)<1e-8), logloss(pm)<logloss(po))
