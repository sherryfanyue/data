import sys
import io
import pandas as pd
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

df = pd.read_csv('vgsales.csv')
print(df.shape)
print(df.describe())
print(df.values)

dfs = pd.read_csv(df.shape)
dfd = df.describe()
dfv = pd.read_csv(df.values)

dfd.to_csv("analyse.csv")
dfs.to_csv("analyse.csv")
dfv.to_csv("analyse.csv")

with open("analyse1.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(dfs)
