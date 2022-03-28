import pandas as pd


data = pd.read_json('/home/blackheart/Documents/Programming/Learn-Python/Pandas/files/data.json')

print(data.head())
print(data.head(100))

print(data.tail())
print(data.tail(100))

print(data.info())

