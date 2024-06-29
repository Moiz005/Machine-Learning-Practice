import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

df = pd.read_csv('Position_Salaries.csv')
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values
# y = y.reshape(len(y), 1)

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)

y_pred = regressor.predict(X_grid)
plt.scatter(X, y, color="red")
plt.plot(X_grid, y_pred, color='blue')
plt.title('Decision Tree Prediction')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()