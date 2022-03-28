import pandas as pd


data = pd.read_csv(filepath.extension)

print(data.to_string())

data["Date"] = pd.to_datetime(data["Date"])

print(data.to_string())

data.dropna(subset=['Date'], inplace=True)

