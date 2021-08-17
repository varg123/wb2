# Материал браслета Материал браслета, ремешка
def set_mater_br(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Материал браслета' in params):
        if data.get('param').get('Материал браслета'):
            result_data['addin'].append({
                'type': "Материал браслета",
                'params': [{
                    "value": data.get('param').get('Материал браслета')
                }]
            })
        else:
            result_data['addin'].append({
                'type': "Материал браслета",
                'params': [{
                    "value": 'в описании'
                }]
            })
    if params and ('Материал браслета, ремешка' in params):
        if data.get('param').get('Материал браслета'):
            result_data['addin'].append({
                'type': "Материал браслета, ремешка",
                'params': [{
                    "value": data.get('param').get('Материал браслета')
                }]
            })
        else:
            result_data['addin'].append({
                'type': "Материал браслета, ремешка",
                'params': [{
                    "value": 'в описании'
                }]
            })
