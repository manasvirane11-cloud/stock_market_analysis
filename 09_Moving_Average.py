import pandas as pd
df=pd.read_csv("Dataset/stock_data.csv")
df["MA_3"]=df["Close"].rolling(2).mean()
print(df)