import pandas as pd, numpy as np
df=pd.read_csv("Dataset/stock_data.csv")
df.loc[2,"Close"]=np.nan
print(df.isnull().sum())
df["Close"]=df["Close"].fillna(df["Close"].mean())
#print(df)