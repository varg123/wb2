# Цифры
def set_cifr(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Цифры' in params):
        if data.get('param').get('Оформление цифр'):
            result_data['addin'].append({
                'type': "Цифры",
                'params': [
                    {
                        "value": data.get('param').get('Оформление цифр')
                    }
                ]
            })
