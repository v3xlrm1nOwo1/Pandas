
# pip install pandas

import pandas

data = {
	"cars": ["Volvo", "BMW", "Ford"],
	"passings": [34, 6, 78]
}

df = pandas.DataFrame(data)
print(df)


import pandas as pd

data = {
	"cars": ["Volvo", "BMW", "Ford"],
	"passings": [34, 6, 78]
}

df = pd.DataFrame(data)
print(df)


print(pd.__version__)

