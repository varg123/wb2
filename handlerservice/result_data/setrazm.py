from dictservice import DictService




razm = {
    '6 мм': {
        'r': '6 мм',
        'rr': '6'
    },
    '8 мм': {
        'r': '8 мм',
        'rr': '8'
    },
    '10 мм': {
        'r': '10 мм',
        'rr': '10'
    },
    '12 мм': {
        'r': '12 мм',
        'rr': '12'
    },
    '14 мм': {
        'r': '14 мм',
        'rr': '14'
    },
    '16 мм': {
        'r': '16 мм',
        'rr': '16'
    },
    '18 мм': {
        'r': '18 мм',
        'rr': '18'
    },
    '20 мм': {
        'r': '20 мм',
        'rr': '20'
    },
    '22 мм': {
        'r': '22 мм',
        'rr': '22'
    },
    '24 мм': {
        'r': '24 мм',
        'rr': '24'
    },
    '26 мм': {
        'r': '26 мм',
        'rr': '26'
    },
    '28 мм': {
        'r': '28 мм',
        'rr': '28'
    },
    '30 мм': {
        'r': '30 мм',
        'rr': '30'
    },
    '33 мм': {
        'r': '33,5 мм',
        'rr': '33,5'
    },
    '20х16 мм': {
        'r': '20 мм',
        'rr': '20'
    },
    '20х20 мм': {
        'r': '20 мм',
        'rr': '20'
    },
    '22х18 мм': {
        'r': '22 мм',
        'rr': '22'
    },
    '22х22 мм': {
        'r': '22 мм',
        'rr': '22'
    },
    '24х20 мм': {
        'r': '24 мм',
        'rr': '24'
    },
    '24х24 мм': {
        'r': '24 мм',
        'rr': '24'
    },
}


# Бренд
def set_razm(result_data, data):
    dl = data.get('param').get('Ширина ремешка')
    if 'Браслеты для часов' == result_data.get('object') and dl:
        result_data['nomenclatures'][0]['variations'][0]['addin'].append(
            {
                "type": "Размер",
                "params": [
                    {
                        "value": razm.get(dl).get('r')
                    }
                ]
            },
        )
        if razm.get(dl):
            result_data['nomenclatures'][0]['variations'][0]['addin'].append(
                {
                    "type": "Рос. размер",
                    "params": [
                        {
                            "value": razm.get(dl).get('rr')
                        }
                    ]
                },
            )
