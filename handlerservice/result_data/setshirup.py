# Ширина упаковки
def set_shir_up(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Ширина упаковки' in params):
        if data.get('width'):
            result_data['addin'].append({
                'type': "Ширина упаковки",
                'params': [
                    {
                        "count": float(data.get('width'))
                    }
                ]
            })
        else:
            result_data['addin'].append({
                'type': "Ширина упаковки",
                'params': [
                    {
                        "count": 0
                    }
                ]
            })
