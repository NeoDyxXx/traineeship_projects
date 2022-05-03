import json


with open('json_data/json_data0.json', 'r', encoding='utf-8') as f:
    print(json.load(f))