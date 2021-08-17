# TODO: сделать из списка color
def set_nomenclatures_color(result_data, data):
    if result_data.get('object') == 'Будильники электронные':
        return result_data

    is_osn = True

    config = BaseConfig()
    color_br = data.get('param').get('Цвет ремня/браслета')
    if color_br and CatalogsRequest(config).get_from_directory('/colors', pattern=color_br).getData():
        color_br = CatalogsRequest(config).get_from_directory('/colors', pattern=color_br).getData()[0]['key']
    else:
        color_br = None

    color_cif = data.get('param').get('Цвет циферблата')
    if color_cif and CatalogsRequest(config).get_from_directory('/colors', pattern=color_cif).getData():
        color_cif = CatalogsRequest(config).get_from_directory('/colors', pattern=color_cif).getData()[0]['key']
    else:
        color_cif = None

    if color_br:
        result_data['nomenclatures'][0]['addin'].append(
            {
                "type": "Основной цвет",
                "params": [
                    {
                        "value": color_br
                    }
                ]
            }
        )
        is_osn = False
    if color_cif:
        if is_osn:
            result_data['nomenclatures'][0]['addin'].append(
                {
                    "type": "Основной цвет",
                    "params": [
                        {
                            "value": color_cif
                        }
                    ]
                }
            )
        else:
            result_data['nomenclatures'][0]['addin'].append(
                {
                    "type": "Доп. цвета",
                    "params": [
                        {
                            "value": color_cif
                        }
                    ]
                }
            )
    return result_data
