import pandas as pd, numpy as np
df=pd.read_csv("Dataset/stock_data.csv")
print(np.mean(df["Close"]))
print(np.max(df["Close"]))
print(np.min(df["Close"]))
print(np.std(df["Close"]))