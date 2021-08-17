# Форма корпуса
def set_forma(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Форма корпуса' in params):
        if data.get('param').get('Форма'):
            result_data['addin'].append({
                'type': "Форма корпуса",
                'params': [
                    {
                        "value": data.get('param').get('Форма')
                    }
                ]
            })
