import pandas as pd


data = pd.read_csv(filepath.extension)

print(data.to_string())

data.loc[7, 'Duration'] = 45


for i in data.index:
	if data[i, "Duration"] > 120:
		data.loc[i, "Duration"] = 120


for i in data.index:
	if data[i, "Duration"] > 120:
		data.drop(i, inplace=True)

		