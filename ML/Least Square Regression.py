import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('placement_cgpa.csv')

print(df.shape)

df.head(100)

plt.scatter(df['cgpa'],df['package'])
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')

X = df.iloc[:,0:1]
print(X)

y = df.iloc[:,-1]

print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train,y_train)

print(X_test)

print(y_test)

print("cgpa:",X_test.iloc[0].values)
lr.predict(X_test.iloc[0].values.reshape(1,1))

y_pred = lr.predict(X_test)
print(y_pred)

plt.scatter(df['cgpa'],df['package'])
plt.plot(X_train,lr.predict(X_train),color='red')
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')

m = lr.coef_
print(m)

b = lr.intercept_
print(b)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Assuming you already have y_test and y_pred from the previous example

# Calculate the error metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display the error values
print(f'Mean Absolute Error: {mae:.2f}')
print(f'Mean Squared Error: {mse:.2f}')
print(f'Root Mean Squared Error: {rmse:.2f}')
print(f'R-squared: {r2:.2f}')

# y = mx + b

print("package:",m * 8.58 + b)

print("Package:",lr.predict([[8.58]]))

print("package:",m * 9.5 + b)

print("package:",lr.predict([[9.5]]))
plt.show()