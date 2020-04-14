
#1. Split the data into 75% train / 25% test 

# from sklearn.cross_validation import train_test_split
# Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,
#                                                 random_state=0)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=0)

#2. Create a GaussianNB model based on training data
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)

#Note: if error: you may need np.asarray(...,dtype=np.float64)

#3. Test it on test data
from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)