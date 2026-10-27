import pandas as pd
df=pd.read_csv("Dataset/stock_data.csv")
print(df[df["Close"]>115])