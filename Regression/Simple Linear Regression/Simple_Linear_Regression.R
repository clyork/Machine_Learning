###Simple Linear Regression###
dataset = read.csv('/Users/codyyork/Desktop/Programming Projects/Machine Learning/Regression/Simple Linear Regression/Salary_Data.csv')
#dataset = dataset[, 2:3]

##Splitting the dataset into Training and Testing##
#install.packages('caTools')
library(caTools)
#set seed if you want the same values
#set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

##Fitting Simple Linear Regression to the Training set##
# ~ means proportional to
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)
#in console "summary(regressor)" for more info

##Predicting the Test set results##
y_pred = predict(regressor, newdata = test_set)
y_pred_training = predict(regressor, newdata = training_set)

##Visualizing the Training set results##
#install packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = y_pred_training),
            color = 'blue') +
  ggtitle('Salary vs Experience (Training Set)') +
  xlab('Years of Experience') +
  ylab('Salary')

##Visualizing the Testing set results##
#install packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = y_pred_training),
            color = 'blue') +
  ggtitle('Salary vs Experience (Test Set)') +
  xlab('Years of Experience') +
  ylab('Salary')




