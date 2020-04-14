
from sklearn.model_selection import GridSearchCV
#set params as a dictionary
param_grid = {'kernel': ('linear','poly', 'rbf', 'sigmoid'),
              'degree': [1, 3, 5],
              'shrinking': [True, False],
              'C':[1, 7]}
grid = GridSearchCV(SVC(), param_grid, cv=5)

grid.fit(Xtrain, ytrain);