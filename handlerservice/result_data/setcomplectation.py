from dictservice import DictService


# Комплектация
def set_complplectation(result_data, data):
    params = data.get('categori_props').keys()
    compl_dict = DictService.getDict('compl')
    if params and ('Комплектация' in params):
        if data.get('param').get('Комплектность') and compl_dict.get(data.get('param').get('Комплектность')):
            params_arr = compl_dict.get(data.get('param').get('Комплектность')).split(',')
            res = []
            i = 1
            for p in params_arr:
                res.append({
                    "value": p
                })
                i += 1
                if i == 10:
                    break
            result_data['addin'].append({
                'type': "Комплектация",
                'params': res
            })
        else:
            result_data['addin'].append({
                'type': "Комплектация",
                'params': [
                    {
                        "value": 'в описанании'
                    }
                ]
            })
