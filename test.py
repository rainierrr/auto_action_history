import pandas as pd

df = pd.read_csv("plans_csv.csv")
print(list(df.iloc[:,0]))
print(df)