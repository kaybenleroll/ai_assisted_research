library(MASS)
out <- Sys.getenv('EXAMPLE_OUT', unset=tempdir())
check_sha256 <- function(path, expected) {
 actual <- strsplit(system2('sha256sum', shQuote(path), stdout=TRUE), ' +')[[1]][1]
 stopifnot(identical(actual,expected))
}
check_sha256('data/penguins.csv','f204db2c753b0937caac3cb35258562c14f073e4bbc76be24b4c51ce22767a93')
check_sha256('data/salamanders-package.csv','1dadca43a8c917da58cd341fb04f15c0ad22384a8487a33dc3f6b77516bf8874')
options(digits=10, width=160)
set.seed(467)
p <- read.csv('data/penguins.csv', na.strings='NA')
p$species <- factor(p$species, levels=c('Adelie','Chinstrap','Gentoo'))
p$island <- factor(p$island, levels=c('Biscoe','Dream','Torgersen'))
p$sex <- factor(p$sex, levels=c('female','male'))
p342 <- p[complete.cases(p[c('body_mass_g','species')]), ]
p333 <- p[complete.cases(p[c('body_mass_g','species','sex')]), ]
stopifnot(nrow(p342)==342, nrow(p333)==333)
g <- glm(body_mass_g ~ species, data=p342, family=gaussian())
a <- glm(body_mass_g ~ species, data=p342, family=Gamma(link='log'))
gs <- glm(body_mass_g ~ species + sex, data=p333, family=gaussian())
as <- glm(body_mass_g ~ species + sex, data=p333, family=Gamma(link='log'))
stopifnot(all(c(g$converged,a$converged,gs$converged,as$converged)))
mm <- model.matrix(~ species * island, p342)
main <- model.matrix(~ species + island, p342)
stopifnot(qr(mm)$rank==5, ncol(mm)==9, qr(main)$rank==5, ncol(main)==5)
cat('PENGUINS n=', nrow(p342), 'sex subset=', nrow(p333), '\n')
cat('PENGUINS species island interaction rank/columns=', qr(mm)$rank, ncol(mm), '\n')
cat('PENGUINS species island main rank/columns=', qr(main)$rank, ncol(main), '\n')
print(table(p342$species,p342$island)); print(coef(g)); print(coef(a)); print(coef(gs)); print(coef(as))
cat('PENGUINS species fitted means g, gamma; gaussian residual sd, gamma dispersion\n')
newp <- data.frame(species=factor(c('Adelie','Chinstrap','Gentoo'), levels=levels(p$species)))
print(data.frame(species=newp$species, gaussian=predict(g,newp,type='response'), gamma=predict(a,newp,type='response')))
stopifnot(max(abs(predict(g,newp,type='response')-c(3700.6623,3733.0882,5076.0163)))<.01, max(abs(predict(g,newp,type='response')-predict(a,newp,type='response')))<.01)
print(c(gaussian_residual_sd=sqrt(summary(g)$dispersion), gamma_dispersion=summary(a)$dispersion))

s <- read.csv('data/salamanders-package.csv')
s <- s[s$spp == 'GP', ]
s$site <- factor(s$site)
s$mined <- factor(s$mined, levels=c('no','yes'))
stopifnot(nrow(s)==92, nlevels(s$site)==23, all(table(s$site)==4), !anyNA(s[c('count','mined','DOP')]))
cat('SALAMANDERS GP sites and rows by mined\n'); print(table(s$mined)); print(table(unique(s[c('site','mined')])$mined))
cat('SALAMANDERS GP count summary by mined\n'); print(tapply(s$count,s$mined,summary)); print(tapply(s$count,s$mined,var))
cat('SALAMANDERS DOP summary, correlation with mined indicator\n'); print(summary(s$DOP)); print(cor(s$DOP,as.numeric(s$mined=='yes')))
po <- glm(count ~ mined + DOP, data=s, family=poisson())
nb <- glm.nb(count ~ mined + DOP, data=s, control=glm.control(maxit=100))
stopifnot(po$converged,nb$converged,abs(nb$theta-1.7314)<.01)
cat('SALAMANDERS fits poisson, nb coefficients and standard errors\n'); print(coef(summary(po))); print(coef(summary(nb)))
cat('SALAMANDERS poisson Pearson/df, NB theta, NB Pearson/df\n'); print(c(poisson_pearson=sum(residuals(po,type='pearson')^2)/df.residual(po), nb_theta=nb$theta, nb_pearson=sum(residuals(nb,type='pearson')^2)/df.residual(nb)))
new <- data.frame(mined=factor(c('no','yes'),levels=levels(s$mined)), DOP=0)
cat('SALAMANDERS predicted counts DOP 0\n'); print(data.frame(mined=new$mined,poisson=predict(po,new,type='response'),nb=predict(nb,new,type='response')))
# Fixed random row test and site-blocked test: same approximate test fraction.
site_order <- sort(unique(as.character(s$site)))
held_sites <- site_order[c(2,6,10,14,18,22)]
set.seed(467); row_test <- sort(sample(seq_len(nrow(s)),24))
split <- list(row=row_test, site=which(as.character(s$site) %in% held_sites))
results <- data.frame()
for (kind in names(split)) {
 test <- split[[kind]]; train <- setdiff(seq_len(nrow(s)),test)
 f <- glm(count ~ mined + DOP,data=s[train,],family=poisson())
 n <- glm.nb(count ~ mined + DOP,data=s[train,],control=glm.control(maxit=100))
 stopifnot(f$converged,n$converged)
 for (model in c('poisson','nb')) {
  fit <- if(model=='poisson') f else n
  mu <- predict(fit,newdata=s[test,],type='response'); y <- s$count[test]
  lp <- if(model=='poisson') dpois(y,mu,log=TRUE) else dnbinom(y,mu=mu,size=n$theta,log=TRUE)
  results <- rbind(results,data.frame(split=kind,model=model,train_n=length(train),test_n=length(test),heldout_sites=length(unique(s$site[test])),overlap_sites=length(intersect(s$site[train],s$site[test])),MAE=mean(abs(y-mu)),mean_log_score=mean(lp)))
 }
}
stopifnot(all(results$overlap_sites[results$split=='site']==0), all(results$overlap_sites[results$split=='row']>0), all(is.finite(results$mean_log_score)))
cat('SALAMANDERS held sites:',paste(held_sites,collapse=', '),'\n'); print(results,row.names=FALSE)
write.csv(results,file.path(out,'real-case-validation.csv'),row.names=FALSE)
model_rows <- function(fit, dataset, name) {
 z <- coef(summary(fit))
 data.frame(dataset=dataset, model=name, term=rownames(z), estimate=z[,1], standard_error=z[,2], row.names=NULL)
}
coefficients <- rbind(model_rows(g,'penguins342','gaussian'),model_rows(a,'penguins342','gamma_log'),model_rows(gs,'penguins333','gaussian_sex'),model_rows(as,'penguins333','gamma_log_sex'),model_rows(po,'salamanders_GP92','poisson'),model_rows(nb,'salamanders_GP92','nb2'))
write.csv(coefficients,file.path(out,'real-case-coefficients.csv'),row.names=FALSE)
predictions <- rbind(data.frame(dataset='penguins342',scenario=as.character(newp$species),poisson_or_gaussian=predict(g,newp,type='response'),nb_or_gamma=predict(a,newp,type='response')),data.frame(dataset='salamanders_GP92',scenario=as.character(new$mined),poisson_or_gaussian=predict(po,new,type='response'),nb_or_gamma=predict(nb,new,type='response')))
write.csv(predictions,file.path(out,'real-case-predictions.csv'),row.names=FALSE)
