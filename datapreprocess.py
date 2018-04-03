import pandas as pd
from sklearn.preprocessing import Imputer

FILE = 'data/datapreprocess.csv'


def transform_data(x):
    imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imputer = imputer.fit(x[:, 1:3])
    x[:, 1:3] = imputer.transform(x[:, 1:3])

    return x


dataset = pd.read_csv(FILE)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

print(x)
x = transform_data(x)

print(x)
