import pandas as pd
df=pd.read_csv("Dataset/stock_data.csv")
df["Daily_Return"]=(df["Close"]-df["Open"])/df["Open"]*100
print(df)