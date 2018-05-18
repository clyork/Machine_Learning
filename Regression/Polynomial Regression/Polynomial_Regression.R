###Polynomial Regression###
dataset = read.csv('/Users/codyyork/Documents/GitHub/Machine_Learning/Regression/Polynomial Regression/Position_Salaries.csv')
dataset = dataset[, 2:3]

##Fitting Polynomial Regression to the dataset##
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_regressor = lm(formula = Salary ~ .,
                    data = dataset)

##Visualizing the Polynomial Regression Results##
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(poly_regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff (Polynomial Regression) R') +
  xlab('Level') +
  ylab('Salary')