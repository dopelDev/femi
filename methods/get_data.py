import pandas as pd
from typing import NamedTuple

# push data to app.py

def push_data_totales():
    data = pd.read_csv('static/data/totales_por_departamento.csv')
    labels_tmp = [value[0] for value in data.iloc[:,:1].values]
    values = [value[0] for value in data.iloc[:,1:2].values]
    labels = []
    for item in labels_tmp:
        labels.append(item)
    
    data_delivery = {'labels': labels, 'values' : values}
    return data_delivery

def push_data_totales_line():
    data = pd.read_csv('static/data/clean_data.csv', index_col='VÍCTIMAS DE FEMINICIDIO, SEGÚN DEPARTAMENTO, 2015 - 2019')
    labels = data.iloc[:1, 2:].values.tolist()[0]
    values = data.iloc[1:2,2:].values.tolist()[0]
    
    data_delivery = {'labels': labels, 'values' : values}
    return data_delivery

def push_data_cusco_la_libertad():
    data = pd.read_csv('static/data/cusco_la_libertad.csv')
    labels_tmp = [value[0] for value in data.iloc[:,:1].values]
    values = [value[0] for value in data.iloc[:,1:2].values]
    labels = []
    for item in labels_tmp:
        labels.append(item)
    
    data_delivery = {'labels': labels, 'values' : values}
    return data_delivery

def push_data_top_5_2018():
    data = pd.read_csv('static/data/sorting_2018.csv')
    labels_tmp = [value[0] for value in data.iloc[:,:1].values]
    values = [value[0] for value in data.iloc[:,1:2].values]
    labels = []
    for item in labels_tmp:
        labels.append(item)
    
    data_delivery = {'labels': labels, 'values' : values}
    return data_delivery

def push_data_top_10_totales():
    data = pd.read_csv('static/data/totales_por_departamento.csv')
    labels_tmp = [value[0] for value in data.iloc[:,:1].values]
    values = [value[0] for value in data.iloc[:,1:2].values]
    labels = []
    for item in labels_tmp:
        labels.append(item)
    
    data_delivery = {'labels': labels, 'values' : values}
    return data_delivery


