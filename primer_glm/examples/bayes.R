# Bounded educational samplers. These diagnostics do not certify general convergence.
set.seed(467)
x<-c(-2,-1.5,-1,-.5,0,.5,1,1.5,2,2.5)
y<-c(0,1,0,0,1,0,1,1,0,1)
logpost<-function(b) {eta<-b[1]+b[2]*x; sum(dbinom(y,1,plogis(eta),log=TRUE))+sum(dnorm(b,0,2,log=TRUE))}
grid<-seq(-6,6,length.out=241); cells<-expand.grid(a=grid,b=grid)
lw<-vapply(seq_len(nrow(cells)),function(i) logpost(c(cells$a[i],cells$b[i])),numeric(1))
w<-exp(lw-max(lw)); w<-w/sum(w)
target<-c(intercept=sum(w*cells$a),slope=sum(w*cells$b),pred=sum(w*plogis(cells$a+cells$b)))
starts<-rbind(c(-3,-2),c(-2,3),c(2,-3),c(3,2)); n<-30000L; burn<-5000L
result<-matrix(NA_real_,4,3); accepts<-numeric(4); ac1<-numeric(4); batch_variance<-numeric(4)
for(k in 1:4){
 current<-starts[k,]; lp<-logpost(current); trace<-matrix(NA_real_,n,2); accepted<-0L
 for(i in 1:n){
  proposal<-current+rnorm(2,sd=.7); lnew<-logpost(proposal)
  if(log(runif(1))<lnew-lp){current<-proposal; lp<-lnew; accepted<-accepted+1L}
  trace[i,]<-current
 }
 kept<-trace[(burn+1):n,,drop=FALSE]; result[k,]<-c(colMeans(kept),mean(plogis(kept[,1]+kept[,2])))
 accepts[k]<-accepted/n; ac1[k]<-cor(kept[-nrow(kept),1],kept[-1,1])
 pred_draws<-plogis(kept[,1]+kept[,2]); batch_means<-colMeans(matrix(pred_draws,nrow=500))
 batch_variance[k]<-var(batch_means)/length(batch_means)
}
pooled<-colMeans(result)
mcse<-sqrt(sum(batch_variance)/16)
cat('grid_target',target,'mcmc_pooled',pooled,'acceptance',accepts,'lag1_intercept',ac1,'predictive_batch_mcse',mcse,'grid_difference',pooled[3]-target[3],'\n')
stopifnot(all(accepts>.15 & accepts<.85),max(abs(pooled-target))<.09,max(apply(result,2,function(z)diff(range(z))))<.16)
# Beta-binomial hierarchy: mu~Beta(2,2), theta_j|mu~Beta(6mu,6(1-mu)).
# Exact conditional beta distributions and numerical 1D integration over mu.
success<-c(1,4,7,9); trials<-rep(10,4); mu<-seq(.0001,.9999,length.out=5000); conc<-6
lp<-dbeta(mu,2,2,log=TRUE)
for(j in seq_along(success)) lp<-lp+lbeta(conc*mu+success[j],conc*(1-mu)+trials[j]-success[j])-lbeta(conc*mu,conc*(1-mu))
ww<-exp(lp-max(lp)); ww<-ww/sum(ww)
target_theta<-vapply(seq_along(success),function(j)sum(ww*(conc*mu+success[j])/(conc+trials[j])),numeric(1))
draw_mu<-sample(mu,40000,replace=TRUE,prob=ww)
draw_theta<-sapply(seq_along(success),function(j) rbeta(length(draw_mu),conc*draw_mu+success[j],conc*(1-draw_mu)+trials[j]-success[j]))
actual<-colMeans(draw_theta)
cat('hierarchical_conditional_target',target_theta,'sample_means',actual,'raw_proportions',success/trials,'\n')
stopifnot(max(abs(actual-target_theta))<.01,target_theta[1]>.1,target_theta[4]<.9)

# Prior sensitivity and predictive distributions for the SAME ten observations.
set.seed(470)
S<-30000L
sensitivity<-function(sd,cells_used=cells) {
 logw<-vapply(seq_len(nrow(cells_used)),function(i) {b<-c(cells_used$a[i],cells_used$b[i]); eta<-b[1]+b[2]*x; sum(dbinom(y,1,plogis(eta),log=TRUE))+sum(dnorm(b,0,sd,log=TRUE))},numeric(1))
 weight<-exp(logw-max(logw));weight<-weight/sum(weight)
 sum(weight*plogis(cells_used$a+cells_used$b))
}
pred_by_prior<-vapply(c(1,2,3),sensitivity,numeric(1))
expanded<-expand.grid(a=seq(-8,8,by=.05),b=seq(-8,8,by=.05))
expanded_prediction<-sensitivity(3,expanded)
cat("prior_sd3_expanded_grid_prediction",expanded_prediction,"difference",abs(expanded_prediction-pred_by_prior[3]),"\n")
stopifnot(abs(expanded_prediction-pred_by_prior[3])<1e-3)
# Normal priors N(0,2^2) with the same design and observation statistic.
prior_b<-matrix(rnorm(2*S,0,2),ncol=2)
prior_p<-plogis(outer(prior_b[,1],rep(1,length(x)))+outer(prior_b[,2],x))
prior_y<-matrix(rbinom(S*length(x),1,as.vector(prior_p)),nrow=S)
prior_extreme<-mean(rowSums(prior_y)==0 | rowSums(prior_y)==length(x))
indices<-sample.int(nrow(cells),S,replace=TRUE,prob=w)
post_p<-plogis(outer(cells$a[indices],rep(1,length(x)))+outer(cells$b[indices],x))
post_y<-matrix(rbinom(S*length(x),1,as.vector(post_p)),nrow=S)
observed_count<-sum(y); post_tail<-mean(rowSums(post_y)>=observed_count)
observed_gradient<-sum(y[x>0])-sum(y[x<0])
rep_gradient<-rowSums(post_y[,x>0,drop=FALSE])-rowSums(post_y[,x<0,drop=FALSE])
post_gradient_tail<-mean(abs(rep_gradient)>=abs(observed_gradient))
cat('prior_scales_1_2_3_prediction',pred_by_prior,'prior_extreme_probability',prior_extreme,'observed_count',observed_count,'posterior_count_upper_tail',post_tail,'observed_gradient',observed_gradient,'posterior_absolute_gradient_tail',post_gradient_tail,'\n')
stopifnot(all(is.finite(pred_by_prior)),prior_extreme>0,post_tail>0,post_tail<1,post_gradient_tail>0,post_gradient_tail<=1)
