from dictservice import DictService


# Пол
def set_pol(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Пол' in params):
        if data.get('param').get('Пол'):
            pol_vals = DictService.getDict('pol').get(data.get('param').get('Пол'))
            params_pol = []
            for pol in pol_vals:
                params_pol.append({
                    "value": pol
                })
            result_data['addin'].append({
                'type': "Пол",
                'params': params_pol
            })
        else:
            pol_vals = DictService.getDict('pol').get('унисекс')
            params_pol = []
            for pol in pol_vals:
                params_pol.append({
                    "value": pol
                })
            result_data['addin'].append({
                'type': "Пол",
                'params': params_pol
            })
