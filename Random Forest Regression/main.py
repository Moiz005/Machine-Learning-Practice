import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('Position_Salaries.csv')
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)

y_pred = regressor.predict(X)
y = y.reshape(len(y), 1)
y_pred = y_pred.reshape(len(y), 1)
from sklearn.metrics import r2_score
print(r2_score(y, y_pred))
