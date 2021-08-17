# Доп. опции
def set_dop_opt(result_data, data):
    op = [
        data.get('param').get('Функции'),
        data.get('param').get('Батарея'),
        data.get('param').get('Индикатор даты'),
        data.get('param').get('Подсветка'),
        data.get('param').get('Календарь'),
        data.get('param').get('Таймеры'),
    ]
    params_res = []
    i = 1
    for p in op:
        if p:
            params_res.append({
                "value": p
            })
            i += 1
            if i == 3:
                break
    params = data.get('categori_props').keys()
    if len(params_res):
        is_set = False
        if (not is_set) and params and ('Доп. опции часов' in params):
            result_data['addin'].append(
                {
                    "type": "Доп. опции часов",
                    "params": params_res
                }
            )
            is_set = True
        if (not is_set) and params and ('Доп. опции прибора' in params):
            result_data['addin'].append(
                {
                    "type": "Доп. опции прибора",
                    "params": params_res
                }
            )
            is_set = True
        if (not is_set) and params and ('Доп. опции интерьерных часов' in params):
            result_data['addin'].append(
                {
                    "type": "Доп. опции интерьерных часов",
                    "params": params_res
                }
            )
            is_set = True
        if (not is_set) and params and ('Особенности часов' in params):
            result_data['addin'].append(
                {
                    "type": "Особенности часов",
                    "params": params_res[:3]
                }
            )
            is_set = True
