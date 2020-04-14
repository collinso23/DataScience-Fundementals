#Fitting multidim data
rng = np.random.RandomState(1)

 
#Exercise: 

# 1) Create X that is random values of shape 100 by 3. 
# Populate it with random samples from a uniform distribution over ``[0, 10)``
#See rand or example above
X = 10 * rng.rand(100, 3)
y = 0.5 + np.dot(X, [1.5, -2., 1.])

#2) create a lin reg model on the multi dim data
model.fit(X, y)

#3) print estimates
print(model.intercept_)
print(model.coef_)