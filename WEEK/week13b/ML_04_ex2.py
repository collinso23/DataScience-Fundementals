from sklearn.linear_model import LinearRegression
X = x[:, np.newaxis]

model = LinearRegression().fit(X, y)
yfit = model.predict(X)
plt.scatter(x, y, c='k')
plt.plot(x, yfit);