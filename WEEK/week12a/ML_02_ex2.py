
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,
                                                random_state=0)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)

#Note: if error: you may need np.asarray(...,dtype=np.float64)

# Now that we have predicted our model, we can gauge its accuracy by comparing the true values of the test set to the predictions:

from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)