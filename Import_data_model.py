import pandas as pd

# Load dataset
df = pd.read_csv("cps_00003.dat.gz" compression="gzip")

# data
print(df.head())
print(df.columns)
