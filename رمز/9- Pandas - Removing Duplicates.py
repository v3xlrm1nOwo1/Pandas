import pandas as pd


data = pd.read_csv(filepath.extension)

print(data.to_string())

print(data.duplicated())

data.drop_duplicates(inplace=True)

