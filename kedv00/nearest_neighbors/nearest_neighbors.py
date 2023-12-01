import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create 500 samples with 2 features (x and y-axis), 3 centers with standard deviation 3
X, y = make_blobs(n_samples=500, n_features=2, centers=3, cluster_std=3, random_state=2)

# Dividing data into training sets and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Creating KNeighbor classifiers
knn5 = KNeighborsClassifier(n_neighbors=5)
knn1 = KNeighborsClassifier(n_neighbors=1)

# Training
knn5.fit(X_train, y_train)
knn1.fit(X_train, y_train)

# Testing
y_pred_5 = knn5.predict(X_test)
y_pred_1 = knn1.predict(X_test)

# Measuring accuracy
knn5_accuracy = round(accuracy_score(y_test, y_pred_5), 2)
knn1_accuracy = round(accuracy_score(y_test, y_pred_1), 2)

print("Prediction accuracy knn=5: " + str(knn5_accuracy))
print("Prediction accuracy knn=1: " + str(knn1_accuracy))

# Visualising data
plt.figure(figsize=(10, 10))
plt.scatter(X[:, 0], X[:, 1], c=y, s=50)

plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_5, s=50, edgecolors='black')
plt.title("Predicted values with k=5", fontsize=20)

plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_1, s=50, edgecolors='black')
plt.title("Predicted values with k=1", fontsize=20)
plt.show()
