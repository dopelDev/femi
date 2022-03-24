import pandas as pd
from typing import NamedTuple

# push data to app.py

def push_data_totales():
    data = pd.read_csv('static/data/totales_por_departamento.csv')
    labels_tmp = [value[0] for value in data.iloc[:,:1].values]
    values = [value[0] for value in data.iloc[:,1:2].values]
    labels = []
    for item in labels_tmp:
        labels.append(str(item))
    
    print(labels)
    data_delivery = {'labels': labels, 'values' : values}
    return data_delivery
