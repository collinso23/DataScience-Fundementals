
#1. Create new data points, X2: 100 samples, 2 features. use rng 
# X2 = ?
X2 = rng.randn(100, 2)

#2. Predict the labels
# Instead of fitting; call the predict method and pass the new dataset, X2
#call your predicted labels y2
# y2 = ?
y2 = model.predict(X2)

# plot the model fit
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

ax[0].scatter(X2[:, 0], X2[:, 1], c='gray', s=50)
ax[0].axis([-4, 4, -3, 3])

ax[1].scatter(X2[:, 0], X2[:, 1], c=y2, s=50,
              cmap='viridis', norm=pts.norm)
ax[1].axis([-4, 4, -3, 3])

# format plots
format_plot(ax[0], 'Unknown Data')
format_plot(ax[1], 'Predicted Labels')