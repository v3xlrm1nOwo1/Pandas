import pandas as pd


data = pd.read_json('/home/blackheart/Documents/Programming/Learn-Python/Pandas/files/data.json')

## Remove Rows

new_data = data.dropna()
print(new_data.to_string())

# data.dropna(inplace=True)


## Replace Empty Values

# all file
new_data = data.fillna(99) # inplace=True
print(new_data.to_string())

# just column
new_data = data["Calories"].fillna(99) # inplace=True
print(new_data.to_string())


# 1- mean 
new_data = data["Calories"].fillna(data["Calories"].mean()) # inplace=True
print(new_data.to_string())

# 2- median
new_data = data["Calories"].fillna(data["Calories"].median()) # inplace=True
print(new_data.to_string())

# 3- mode
new_data = data["Calories"].fillna(data["Calories"].mode()) # inplace=True
print(new_data.to_string())


