# Механизм Механизм часов
def set_mech(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Механизм часов' in params):
        if data.get('param').get('Механизм'):
            result_data['addin'].append({
                'type': "Механизм часов",
                'params': [
                    {
                        "value": data.get('param').get('Механизм')
                    }
                ]
            })
