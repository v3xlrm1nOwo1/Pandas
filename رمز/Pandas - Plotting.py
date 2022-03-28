import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/home/blackheart/Documents/Programming/Learn-Python/Pandas/files/data.csv')

print(data)

print(data.to_string())


data.plot()

data.plot(kind='scatter', x='Duration', y='Calories')

data.plot(kind='scatter', x='Duration', y='Maxpulse')

plt.show()

