# Cubic truncated-power spline with an interior knot at x=0.
# Fixed ridge penalty demonstrates basis and penalisation; smoothing is not estimated.
x <- seq(-1.5,1.5,length.out=24)
y <- c(1,2,1,3,0,2,2,1,3,2,4,1,2,4,3,3,5,2,4,5,3,6,4,7)
z <- cbind(x^2,x^3,pmax(x,0)^3); X <- cbind(1,x,z); S <- diag(c(0,0,4,4,4))
objective <- function(b) sum(exp(drop(X%*%b))-y*drop(X%*%b)) + drop(crossprod(b,S%*%b))/2
fit <- optim(rep(0,5),objective,method='BFGS',control=list(reltol=1e-13))
ref <- mgcv::gam(y~x+z, family=poisson(), paraPen=list(z=list(diag(4,3),sp=1)),method='REML')
stopifnot(fit$convergence==0, max(abs(fit$par-coef(ref)))<1e-5)
testx<-c(-.7,.8); pred <- exp(cbind(1,testx,testx^2,testx^3,pmax(testx,0)^3)%*%fit$par)
cat('optim',sprintf('%.10f',fit$par),'mgcv',sprintf('%.10f',coef(ref)),'pred',sprintf('%.10f',pred),'\n')
