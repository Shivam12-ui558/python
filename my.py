import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("Chemistry.Csv")
print(df)

x=df .iloc[: ,0]
y=df .iloc[: ,2]
#print(df.isnull () .sum())
plt.bar(x,y)
plt.show()
