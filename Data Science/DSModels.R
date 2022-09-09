library(ISLR)
library(MASS)
library(class)
library(plotly)
library(tidyverse)

'linear models'
#basic 
fit = lm(brain ~ body, data = Animals) 
summary(fit)
plot(Animals$body, Animals$brain)
abline(fit)

# better
not <- boxplot.stats(Animals$body)$out
animals <- Animals[Animals$body < min(not),]
fit = lm(brain ~ body, data = animals)
summary(fit)
plot(animals$body, animals$brain)
abline(fit)

'logistic regression'
dat <- birthwt
dat$bwt <- NULL
dat$low <- as.factor(dat$low)
dat$race <- factor(dat$race)

lreg <- glm(low ~ .-low, data = dat, family = binomial) ; summary(lreg)
predLR <- predict(lreg, type='response')
predLR2 <- ifelse(predLR > 0.5,1,0)
table(predLR2, dat$low)
mean(predLR2 == dat$low)

'linear discriminant analysis'
dat <- birthwt
dat$bwt <- NULL
dat$low <- as.factor(dat$low)
dat$race <- factor(dat$race)
ldam <- lda(low ~ .-low, data = dat)  ; summary(ldam)
predLDA <- predict(ldam, type='response')
table(predLDA$class, dat$low)

mean(predLDA$class == dat$low)

'time series'

'knn'

'panel data'
