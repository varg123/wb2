# Материал циферблата
def set_mater_cif(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Материал циферблата' in params):
        result_data['addin'].append({
            'type': "Материал циферблата",
            'params': [
                {
                    "value": 'в описании'
                }
            ]
        })
