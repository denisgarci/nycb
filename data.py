import itertools

import pandas as pd
import matplotlib as plt

datas = [pd.read_csv("20{1}-{0:02d} - Citi Bike trip data.csv".format(*date))
    for date in itertools.chain(
        itertools.product(range(7, 13), [13]),
        itertools.product(range(1, 3), [14]))]
data = pd.concat(datas)

data

