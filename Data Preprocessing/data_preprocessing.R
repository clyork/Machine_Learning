### data preprocessing ###

#no need for imports because everything is already imported

##Importing the data##

dataset = read.csv('/Users/codyyork/Desktop/Programming Projects/Machine Learning/Data Preprocessing/Data.csv')
#dataset = dataset[, 2:3]

##Splitting the dataset into Training and Testing##
#install.packages('caTools')
library(caTools)

#set seed if you want the same values
#set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

##Taking care of missing data ##
# dataset$Age = ifelse(is.na(dataset$Age),
#                      ave(dataset$Age, FUN = function(x)mean(x, na.rm = TRUE)),
#                      dataset$Age)
# dataset$Salary = ifelse(is.na(dataset$Salary),
#                       ave(dataset$Salary, FUN = function(x)mean(x, na.rm = TRUE)),
#                       dataset$Salary)

##Encoding Catagorical Data##
# 
# dataset$Country = factor(dataset$Country,
#                          levels = c('France', 'Spain', 'Germany'),
#                          labels = c(1, 2, 3))
# dataset$Purchased = factor(dataset$Purchased,
#                          levels = c('No', 'Yes'),
#                          labels = c(0, 1))

##Feature Scaling##
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])







