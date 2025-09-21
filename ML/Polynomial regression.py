import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.metrics import r2_score
#from sklearn.pipeline import Pipeline
X = 6 * np.random.rand(200, 1) - 3
    #Generates random numbers uniformly in the range (0,1]
    #Scales all values from (0,1] to [0,6).
    #Shifts the range from [0,6)→[-3,3)

y = 0.8 * X**2 + 0.9 * X + 2 + np.random.randn(200, 1)

# y = 0.8x^2 + 0.9x + 2

print(X)
print(y)

plt.plot(X, y,'b.')
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Train test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)
print(X_train.shape)
print(X_test.shape)

print(X_train)
# Applying linear regression
lr = LinearRegression()

lr.fit(X_train,y_train)

y_pred = lr.predict(X_test)
r2_score(y_test,y_pred)

plt.plot(X_train,lr.predict(X_train),color='r')
plt.plot(X, y, "b.")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Applying Polynomial Linear Regression degree 2
poly = PolynomialFeatures(degree=2,include_bias=True)

X_train_trans = poly.fit_transform(X_train)
print(X_train_trans)
X_test_trans = poly.transform(X_test)

print(X_test_trans)
print(X_train[0])
print(X_train_trans[0])

lr = LinearRegression()
lr.fit(X_train_trans,y_train)

y_pred = lr.predict(X_test_trans)

r2_score(y_test,y_pred)

print(lr.coef_)
print(lr.intercept_)

X_new=np.linspace(-3, 3, 200).reshape(200, 1)
print(X_new)
X_new_poly = poly.transform(X_new)
print(X_new_poly)
y_new = lr.predict(X_new_poly)

plt.plot(X_new, y_new, "r-", linewidth=2, label="Predictions")
plt.plot(X_train, y_train, "b.",label='Training points')
plt.plot(X_test, y_test, "g.",label='Testing points')
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()