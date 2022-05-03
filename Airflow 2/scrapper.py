import requests
import json


def get_data_fbi(count: int):
    data = requests.get('https://api.fbi.gov/@wanted?pageSize={0}&page=1&sort_on=modified&sort_order=desc'.format(count.__str__())).json()

    result_data = {
        'name': 'Kirill Kraynov',
        'status': None,
        'data': []
    }

    for item in data['items']:
        new_data = {
            'uid': item['uid'],
            'aliases': "None",
            'publication': item['publication'],
            'age_min': item['age_min'],
            'age_max': item['age_max'],
            'weight_min': item['weight_min'],
            'weight_max': item['weight_max'],
            'height_min': item['height_min'],
            'height_max': item['height_max'],
            'caution': item['caution'],
            'nationality': item['nationality'],
            'sex': item['sex'],
            'image_url': item['images'][0]['original']
        }

        if item['aliases'] is not None:
            new_data['aliases'] = ", ".join(item['aliases'])

        result_data['data'].append(new_data)

    return result_data