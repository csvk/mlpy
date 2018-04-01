import os
import pandas as pd

ROOT = 'D:/Python/mlpy/'


def set_dir(path=ROOT):
    os.chdir(path)


# Import dataset

set_dir()
dataset = pd.read_csv('data/data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
