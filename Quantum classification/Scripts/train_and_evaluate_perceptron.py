from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True, random_state=0)

# Display training set statistics
print("Training set")
print("X: ", X_train.shape)
print("Y: ", y_train.shape)
unique, counts = np.unique(y_train, return_counts=True)
print('With Cavity:        ', counts[0], '\nWithout Cavity: ', counts[1], '\n')

# Display test set statistics
print("Test set")
print("X: ", X_test.shape)
print("Y: ", y_test.shape)
unique, counts = np.unique(y_test, return_counts=True)
print('With Cavity:         ', counts[0], '\nWithout Cavity: ', counts[1], '\n')

# Train and evaluate the first Perceptron model
model_p = Perceptron(max_iter=50, random_state=0, verbose=True)
model_p.fit(X_train, y_train)
print("Train Set Accuracy: %.2f%%" % (model_p.score(X_train, y_train) * 100.0))
print("Test Set Accuracy: %.2f%%" % (model_p.score(X_test, y_test) * 100.0))

# Predict and evaluate on the test set
y_pred = model_p.predict(X_test)
print("Accuracy: %.2f%%" % (accuracy_score(y_test, y_pred) * 100))
matrix_confusion(y_test, y_pred)

# Train and evaluate a second Perceptron model with more iterations
model_mp = Perceptron(max_iter=1000, random_state=0, verbose=False, alpha=0.0001)
model_mp.fit(X_train, y_train)
print("Train Set Accuracy: %.2f%%" % (model_mp.score(X_train, y_train) * 100.0))
print("Test Set Accuracy: %.2f%%" % (model_mp.score(X_test, y_test) * 100.0))

# Predict and evaluate on the test set
y_pred = model_mp.predict(X_test)
print("Accuracy: %.2f%%" % (accuracy_score(y_test, y_pred) * 100))
matrix_confusion(y_test, y_pred)

# Train and evaluate a third Perceptron model with L2 regularization
model_mp1 = Perceptron(max_iter=1000, random_state=0, verbose=False, alpha=0.000001, penalty='l2')  # Adds L2 penalty
model_mp1.fit(X_train, y_train)
print("Train Set Accuracy: %.2f%%" % (model_mp1.score(X_train, y_train) * 100.0))
print("Test Set Accuracy: %.2f%%" % (model_mp1.score(X_test, y_test) * 100.0))

# Predict and evaluate on the test set
y_pred = model_mp1.predict(X_test)
print("Accuracy: %.2f%%" % (accuracy_score(y_test, y_pred) * 100))
matrix_confusion(y_test, y_pred)
