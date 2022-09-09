library(MASS)
library (ISLR2)
plot(Boston$lstat, Boston$medv) # =
plot(medv~lstat, data = Boston)

##lm(data.frame(Boston$lstat, Boston$medv)) # =
##lm(lstat~medv, data = Boston)

fit1 <- lm(medv~lstat, data = Boston)
summary(fit1)
abline(fit1, col ='red')
confint(fit1)
predict(fit1, data.frame(lstat =c(1)))

v <- c('sim', 'talvez', "não")
contrasts(as.factor(v))
