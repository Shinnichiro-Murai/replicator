import pandas as pd

df = pd.read_csv('result_0.10_0.10_0.90_0.01_0.0021.csv', index_col=0)
index = list(df.tail(1).max()>0.01)
print(df.tail(1))
print(index)
df = df.iloc[:,index]
df[::].to_csv('hogegoge.csv')
