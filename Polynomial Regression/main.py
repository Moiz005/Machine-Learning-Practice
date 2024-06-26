import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Position_Salaries.csv')
X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

poly_reg = PolynomialFeatures(degree=4)
poly_X = poly_reg.fit_transform(X)
regressor = LinearRegression()
regressor.fit(poly_X, y)
y_pred = regressor.predict(poly_X)