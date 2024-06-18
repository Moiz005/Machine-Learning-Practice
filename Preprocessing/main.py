import pandas as pd

# Read the CSV file
df = pd.read_csv("loan_small.csv")

# Columns to fill with mode
col = ["Loan_ID", "Gender", "Area", "Loan_Status"]
df[col] = df[col].fillna(df[col].mode().iloc[0])

# Columns to convert to numeric and fill with mean
col2 = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount"]
df[col2] = df[col2].apply(pd.to_numeric, errors='coerce')  # Convert to numeric, coercing errors to NaN
df[col2] = df[col2].fillna(df[col2].mean())  # Fill NaNs with mean

# Print the DataFrame
# print(df)
print(df.dtypes)
# df[col] = df[col].astype("category")
# for column in col:
#     df[column] = df[column].cat.codes

df2 = pd.read_csv("loan_small.csv")
df2 = pd.get_dummies(df2)
print(df2)

# Zscore Normalization
df3 = pd.read_csv("loan_small.csv")
df3 = df3.dropna()
df3 = df3.iloc[:, 2:5]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
normalized_data = scaler.fit_transform(df3)

# print(normalized_data)

# MinMax Normalization
from sklearn.preprocessing import minmax_scale
df4 = pd.read_csv("loan_small.csv")
df4 = df4.dropna()
df4 = df4.iloc[:, 2:5]
scaler = minmax_scale(df4)
print(scaler)
