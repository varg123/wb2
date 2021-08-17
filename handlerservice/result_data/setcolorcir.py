# Цвет циферблата
def set_color_cir(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Цвет циферблата' in params):
        if data.get('param').get('Цвет циферблата'):
            result_data['addin'].append({
                'type': "Цвет циферблата",
                'params': [
                    {
                        "value": data.get('param').get('Цвет циферблата')
                    }
                ]
            })
