# Класс водонепроницаемости Класс водозащиты
def set_vodo(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Класс водонепроницаемости' in params):
        if data.get('param').get('Класс водозащиты'):
            result_data['addin'].append({
                'type': "Класс водонепроницаемости",
                'params': [
                    {
                        "value": data.get('param').get('Класс водозащиты')
                    }
                ]
            })
