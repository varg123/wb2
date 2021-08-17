# Материал изделия
def set_mater_izd(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Материал изделия' in params):
        result_data['addin'].append({
            'type': "Материал изделия",
            'params': [{
                "value": 'в описании'
            }]
        })
