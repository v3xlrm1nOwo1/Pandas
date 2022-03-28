import pandas as pd

data = [1, 2, 3, 4, 5]

ps = pd.Series(data)
print(ps)

print(ps[0])
print(ps[1])
print(ps[2])

data = [1, 2, 3, 4, 5]

ps = pd.Series(data, index = ['A', 'B', 'C', 'D', 'E'])
print(ps)

print(ps['A'])
print(ps['B'])
print(ps['C'])


data = {"Day-1": 690, "Day-2": 455, "Day-3": 555, "Day-4": 864}
ps = pd.Series(data)
print(ps)

print(ps["Day-1"])
print(ps["Day-2"])
print(ps["Day-3"])


data = {"Day-1": 690, "Day-2": 455, "Day-3": 555, "Day-4": 864}
ps = pd.Series(data, index=["Day-1", "Day-2", "Day-3"])

print(ps)

