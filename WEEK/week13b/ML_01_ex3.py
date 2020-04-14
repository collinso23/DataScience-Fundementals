
import pandas

myframe = pandas.read_csv('diabetes.csv')
print(data.shape)
myframe[:8]



#Study the data:
description = myframe.describe()
print(description)

#Seperate the features and labels
array = data.values
#1. Store the features in X and labels in y
#labels are in the last col.
X = array[1:,0:8]
y = array[1:,8]


#Split the dataset:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# 2. Train
# Is this regression or classification?
# Bring the proper library from above
from sklearn.svm import SVC
# fit the support vector classifier model
clf = SVC(kernel='linear')
get_ipython().run_line_magic('time', 'clf.fit(X_train, y_train)')


get_ipython().run_line_magic('time', 'y_pred = clf.predict(X_test)')

print("Train accuracy is %.2f " % (clf.score(X_train, y_train)*100))
print("Test accuracy is %.2f " % (clf.score(X_test, y_test)*100))