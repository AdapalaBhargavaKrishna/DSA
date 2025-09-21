import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 3 * X.flatten() + 2 + np.random.randn(100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train shape:",X_train.shape)
print("X_test shape:",X_test.shape)
sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, eta0=0.1, learning_rate="constant", random_state=42)
sgd_reg.fit(X_train, y_train)
y_pred = sgd_reg.predict(X_test)
print("Coefficient (slope):", sgd_reg.coef_[0])
print("Intercept:", sgd_reg.intercept_[0])
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
plt.scatter(X, y, color="blue", label="Data")
plt.plot(X_test, y_pred, color="red", label="Regression Line (SGD)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = {
    "Size_sqft": [1000, 1500, 2000, 2500, 3000, 1800],
    "No_of_rooms": [2, 3, 3, 4, 5, 3],
    "Age_years": [10, 5, 20, 15, 8, 12],
    "Price": [200000, 250000, 270000, 350000, 400000, 280000]
}
df = pd.DataFrame(data)
X = df[["Size_sqft", "No_of_rooms", "Age_years"]]
y = df["Price"]
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print("Intercept (b):", model.intercept_)
print("Coefficients (w1, w2, w3):", model.coef_)
print(pd.DataFrame({"Actual Price": y, "Predicted Price": y_pred}))
plt.scatter(y, y_pred, color="blue")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color="red")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()