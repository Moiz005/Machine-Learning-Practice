import pandas as pd

df = pd.read_csv("loan_small.csv")
data = df.copy()
col = ["Gender", "Area", "Loan_Status"]
col2 = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount"]
data[col] = data[col].fillna(data[col].mode().iloc[0])
data[col2] = data[col2].apply(pd.to_numeric, errors="coerce")
data[col2] = data[col2].fillna(data[col2].mean())
data = data.drop(["Loan_ID"], axis=1)
data = pd.get_dummies(data, drop_first=True)
# print(data)

x = data.iloc[:, :-1]
y = data.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)

# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

#Scikit learn Method for handling missing values
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

col1 = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount"]
col3 = ["Gender", "Area"]
df2 = df.copy()
X = df2.iloc[:, :-1]
y = df2.iloc[:, -1]


imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(X[col1])
X[col1] = imputer.transform(X[col1])
# print(df2)

ct = ColumnTransformer([('encoder', OneHotEncoder(), [1, 5])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# print(X)
le = LabelEncoder()
y = le.fit_transform(y)
print(y)