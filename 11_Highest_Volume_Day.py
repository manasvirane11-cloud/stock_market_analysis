import pandas as pd
df=pd.read_csv("Dataset/stock_data.csv")
print(df.loc[df["Volume"].idxmax()])