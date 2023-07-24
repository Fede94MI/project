import pandas as pd
import numpy as np


columnname=["sepal length", "sepal width", "petal length", "petal width", "class"]
iris = pd.read_csv('iris.data', names=columnname)

print(iris.head(5))
print(iris.tail(10))

describ = iris.describe()

print(describ)

