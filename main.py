import matplotlib as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Datasets2\PrimaIndiansDataset.csv")
print(df.tail())
print(df.info())
print(df.describe())