# Материал корпуса
def set_mater_corp(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Материал корпуса' in params):
        if data.get('param').get('Материал корпуса'):
            result_data['addin'].append({
                'type': "Материал корпуса",
                'params': [{
                    "value": data.get('param').get('Материал корпуса')
                }]
            })
        else:
            result_data['addin'].append({
                'type': "Материал корпуса",
                'params': [{
                    "value": 'в описании'
                }]
            })
