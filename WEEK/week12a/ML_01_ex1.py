
## Exercise 1: Predict

#1. Create new data points, X2: 50 samples, but std is higher:0.8. 
X2, _ = make_blobs(n_samples=50, centers=2,
                   random_state=0, cluster_std=0.80)

#2. Predict the labels
# Instead of fitting; call the predict method and pass the new dataset, X2
#call your predicted labels y2
y2 = clf.predict(X2)

# plot the results in 2 figures
point_style = dict(cmap='Paired', s=50)
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

#Plot the new dataset
ax[0].scatter(X2[:, 0], X2[:, 1], c='gray', **point_style)
ax[0].axis([-1, 4, -2, 7])
#Plot the predicted labels
ax[1].scatter(X2[:, 0], X2[:, 1], c=y2, **point_style)
ax[1].contour(xy1, xy2, Z, **line_style)
ax[1].axis([-1, 4, -2, 7])

format_plot(ax[0], 'Unknown Data')
format_plot(ax[1], 'Predicted Labels')