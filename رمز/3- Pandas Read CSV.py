import pandas as pd


csv = pd.read_csv('/home/blackheart/Documents/Programming/Learn-Python/Pandas/files/data.csv')

print(csv)

print(csv.to_string())

print(pd.options.display.max_rows)
pd.options.display.max_rows = 1000
print(pd.options.display.max_rows)

print(csv.to_string())

