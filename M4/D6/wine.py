import pandas as pd
import numpy as np

wine = pd.read_csv('wine.csv', usecols=['density','pH','sulphates','alcohol','quality','type'])

descr = wine.describe()

print(descr)