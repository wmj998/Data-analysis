import pandas as pd

x = [1, 2, 5, 10, 12, 14, 17, 19, 3, 21, 18, 28, 7]
x = pd.Series(x)
s = pd.cut(x, bins=[0, 10, 20, 30])
print(s)
