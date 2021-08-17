# Материал стекла
def set_mater_st(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Материал стекла' in params):
        if data.get('param').get('Стекло'):
            result_data['addin'].append({
                'type': "Материал стекла",
                'params': [
                    {
                        "value": data.get('param').get('Стекло')
                    }
                ]
            })
        else:
            result_data['addin'].append({
                'type': "Материал стекла",
                'params': [
                    {
                        "value": 'стекло'
                    }
                ]
            })
