# Высота упаковки
def set_vis_up(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Высота упаковки' in params):
        if data.get('height'):
            result_data['addin'].append({
                'type': "Высота упаковки",
                'params': [
                    {
                        "count": float(data.get('height'))/10
                    }
                ]
            })
        else:
            result_data['addin'].append({
                'type': "Высота упаковки",
                'params': [
                    {
                        "count": 0
                    }
                ]
            })
