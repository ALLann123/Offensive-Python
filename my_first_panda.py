#!/usr/bin/python3
import pandas as pd
print("Hello, welcome to pandas!!")

data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)