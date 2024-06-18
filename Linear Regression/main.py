import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
X = df[:, :-1]
y = df[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

# Viewing the regression line against training data
plt.scatter(X_train, y_train)
plt.plot(X_train, regressor.predict(X_test))
plt.title('Regression Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Viewing the regression line against testing data
plt.scatter(X_test, y_test)
plt.plot(X_train, regressor.predict(X_test))
plt.title('Regression Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()