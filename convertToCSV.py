# Converts a JSON file to CSV for data analysis
from copy import deepcopy
import pandas
import json
import csv
import os
from pandas import Series, DataFrame
from pandas.io.json import json_normalize 

def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows

def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem

def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '_' + key))
        elif isinstance(data, list):
            rows = []
            if(len(data) != 0):
                for i in range(len(data)):
                    [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
            else:
                data.append("")
                [rows.append(elem) for elem in flatten_list(flatten_json(data[0], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))

f = open(r'data.json')
data = json.load(f) # load as json
f.close()

# normalizing flat json
df = json_to_dataframe(data)
df.to_csv('result.csv', index=False, encoding='utf-8')

