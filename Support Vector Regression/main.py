import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

df = pd.read_csv('data.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
y = y.reshape(len(y), 1)

sc_X = StandardScaler()
sc_y = StandardScaler()

X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

regressor = SVR(kernel="rbf")
regressor.fit(X,y)

y_pred = sc_y.inverse_transform(regressor.predict(sc_X.ttransform([[6.5]])).reshape(-1,1))
y_pred = sc_y.inverse_transform(y_pred)
