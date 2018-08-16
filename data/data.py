import pandas as pd
import numpy as np

import json


def load_data(nhap, xuat, job):
    job = int(job)
    parameters = pd.read_excel(open(nhap,'rb'), sheet_name='Parameters')
    json_parameters = json.loads(parameters.set_index('name')['value'].to_json())
    
    orders = pd.read_excel(open(nhap,'rb'), sheet_name='Orders')
    json_orders = orders.to_dict(orient='list')
    
    sequence = pd.read_excel(open(nhap,'rb'), sheet_name='Sequences')
    sequence = [[int(x) for x in sequence[lst] if ~np.isnan(x)] for lst in range(job)]
    json_sequence = {}
    json_sequence['sequence'] = sequence
    
    processing_time = pd.read_excel(open(nhap,'rb'), sheet_name='ProcessingTime')
    processing_time = [[int(x) for x in processing_time[lst] if ~np.isnan(x)] for lst in range(job)]
    json_processing_time = {}
    json_processing_time['processing_time'] = processing_time
    
    nachines = pd.read_excel(open(nhap,'rb'), sheet_name='Setup')
    json_machines = nachines.to_dict(orient='list')
    
    data = json_parameters.copy()
    data.update(json_orders)
    data.update(json_sequence)
    data.update(json_processing_time)
    data.update(json_machines)
    
    with open(xuat, 'w') as fp:
        json.dump(data, fp)