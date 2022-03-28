import pandas as pd

data = {
	"calories": [540, 350, 430],
	"duration": [60, 30, 45]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[0])
print(df.loc[1])
print(df.loc[[0, 2]])


data = {
	"calories": [540, 350, 430],
	"duration": [60, 30, 45]
}

df = pd.DataFrame(data, index=["A", "B", "C"])
print(df)
print(df.loc["A"])
print(df.loc["B"])
print(df.loc[["A", "C"]])

