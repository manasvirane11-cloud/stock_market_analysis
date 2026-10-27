import pandas as pd
df=pd.read_csv("Dataset/stock_data.csv")
df["Week"]=[1,1,1,1,1,2,2,2,2,2]
#print(df)
print(df.groupby("Week")["Close"].mean())