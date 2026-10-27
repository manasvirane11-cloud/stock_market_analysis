import pandas as pd
df=pd.read_csv("Dataset/stock_data.csv")
df.to_csv("stock_report.csv",index=False)
print("Saved")