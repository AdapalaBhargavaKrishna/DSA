import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Step 1: Generate random data
X = 6 * np.random.rand(200, 1) - 3
y = 0.8 * X**2 + 0.9 * X + 2 + np.random.randn(200, 1)

plt.plot(X, y, 'b.')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Generated Quadratic Data")
plt.show()

# Step 2: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Step 3: Apply Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict on test set
y_pred = lr.predict(X_test)

# Evaluate model performance using R^2 score
print("Linear Regression R^2 score:", r2_score(y_test, y_pred))

# Visualize linear regression fit
plt.plot(X_train, lr.predict(X_train), color='r', label='Linear Fit')
plt.plot(X, y, 'b.', label='Data Points')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression Fit")
plt.legend()
plt.show()

# Step 4: Polynomial Regression (degree 2)
poly = PolynomialFeatures(degree=2, include_bias=True)  # Transform features to include X^2
X_train_trans = poly.fit_transform(X_train)  # Transform training data
X_test_trans = poly.transform(X_test)       # Transform test data

# Train linear regression on transformed features
lr = LinearRegression()
lr.fit(X_train_trans, y_train)

# Predict on test set
y_pred = lr.predict(X_test_trans)

# Evaluate model performance
print("Polynomial Regression R^2 score:", r2_score(y_test, y_pred))

# Step 5: Visualize Polynomial Regression fit
X_new = np.linspace(-3, 3, 200).reshape(200, 1)  # Create smooth X values for plotting
X_new_poly = poly.transform(X_new)               # Transform to polynomial features
y_new = lr.predict(X_new_poly)                   # Predict using polynomial regression

plt.plot(X_new, y_new, "r-", linewidth=2, label="Polynomial Predictions")
plt.plot(X_train, y_train, "b.", label='Training points')
plt.plot(X_test, y_test, "g.", label='Testing points')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Polynomial Regression Fit (Degree 2)")
plt.legend()
plt.show()
