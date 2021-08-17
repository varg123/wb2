from dictservice import DictService


# Тнвэд
def set_tnved(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Тнвэд' in params):
        cat = data.get('object')
        tnved_dict = DictService.getDict('tnved')
        result_data['addin'].append({
            'type': "Тнвэд",
            'params': [
                {
                    "value": tnved_dict.get(cat)
                }
            ]
        })
