import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], index_col=0)
index = list(df.tail(1).max()>0.01)
print(df.tail(1))
print(index)
df = df.iloc[:,index]
df[::].to_csv(str(sys.argv[2])+'.csv')
