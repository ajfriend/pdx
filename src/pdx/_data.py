import pandas as pd
from importlib.resources import files

def get_iris():
    file = files('pdx') / 'data/iris.csv'
    iris = pd.read_csv(file)

    return iris
