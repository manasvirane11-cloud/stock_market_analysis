import pandas as pd
df=pd.read_csv("Dataset/stock_data.csv")
df["Return"]=df["Close"].pct_change()
df["Cumulative_Return"]=(1+df["Return"]).cumprod()-1
print(df)