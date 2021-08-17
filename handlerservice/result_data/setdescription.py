from bs4 import BeautifulSoup
import re


# Описание
def set_description(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Описание' in params):
        if data.get('description'):
            res_str = BeautifulSoup(data.get('description'), "lxml").text
            res_str = (data.get('name') + ". " + res_str)
            reg = re.compile('[^a-zA-ZА-Яа-я0-9\.\,\:\!\?\; ]')

            result_data['addin'].append({
                'type': "Описание",
                'params': [
                    {
                        "value": reg.sub('', res_str)[:1000]
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
