from bs4 import BeautifulSoup
import re


# Описание
def set_description(result_data, data):
    params = data.get('categori_props').keys()
    description = data.get('name') + '.\n'
    for p in data.get('param'):
        value = data.get('param').get(p)
        if '|' in value:
            value = value.replace(' |', ',')
        description += p + ': ' + value + '.\n'
    if params and ('Описание' in params):
        if data.get('description'):
            # res_str = BeautifulSoup(data.get('description'), "lxml").text
            # res_str = (data.get('name') + ". " + res_str)
            # reg = re.compile('[^a-zA-ZА-Яа-я0-9\.\,\:\!\?\; ]')

            result_data['addin'].append({
                'type': "Описание",
                'params': [
                    {
                        "value": description[:1000]
                    }
                ]
            })
        else:
            result_data['addin'].append({
                'type': "Описание",
                'params': [
                    {
                        "value": ""
                    }
                ]
            })
    return result_data
