from entityservice import Catalog


def set_nomenclatures_color(result_data, data):
    if result_data.get('object') == 'Будильники электронные':
        return result_data

    is_osn = True

    color_br = data.get('param').get('Цвет ремня/браслета')
    if color_br and Catalog.get_from_directory('/colors', pattern=color_br):
        color_br = Catalog.get_from_directory('/colors', pattern=color_br)[0]['key']
    else:
        color_br = None

    color_cif = data.get('param').get('Цвет циферблата')
    if color_cif and Catalog.get_from_directory('/colors', pattern=color_cif):
        color_cif = Catalog.get_from_directory('/colors', pattern=color_cif)[0]['key']
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
        # todo:цвета
        elif color_br != color_cif:

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
