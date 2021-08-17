# Глубина упаковки
def set_gl_up(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Глубина упаковки' in params):
        if data.get('length'):
            result_data['addin'].append({
                'type': "Глубина упаковки",
                'params': [
                    {
                        "count": float(data.get('length'))
                    }
                ]
            })
        else:
            result_data['addin'].append({
                'type': "Глубина упаковки",
                'params': [
                    {
                        "count": 0
                    }
                ]
            })
