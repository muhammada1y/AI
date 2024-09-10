import pandas as py

value = [3.1,3,5,7.4,7,0.1,5]
index = ['a','b','c','d','e','f','g']

data = py.Series([value],index)

print(data)