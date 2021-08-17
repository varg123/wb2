import re


# todo: добавить баркоды, добавить проверку битых фото
# Номенклатура Розничная цена Фото
def set_nomenclatures(result_data, data):
    photos = []
    for pict in data.get('picture'):
        photos.append({
            'value': pict
        })
    reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
    if result_data.get('nomenclatures'):
        result_data['nomenclatures'][0]['addin'] = [
            {
                "type": "Фото",
                "params": photos
            },
            {
                "type": "Фото360",
                "params": []
            },
            {
                "type": "Видео",
                "params": []
            }
        ]
        result_data['nomenclatures'][0]['variations'][0]['addin'] = [
            {
                "type": "Розничная цена",
                "params": [
                    {
                        "count": float(data.get('price'))
                    }
                ]
            },
        ]
        data['barcode'] = result_data['nomenclatures'][0]['variations'][0]['barcodes'][0]
    else:
        barcode = Barcode().get_barcode()
        data['barcode'] = barcode

        result_data['nomenclatures'] = [
            {

                "vendorCode": data.get('param').get('Код товара'),
                "variations": [
                    {
                        "barcode": barcode,
                        "addin": [
                            {
                                "type": "Розничная цена",
                                "params": [
                                    {
                                        "count": float(data.get('price'))
                                    }
                                ]
                            },
                        ]
                    }
                ],
                "addin": [
                    {
                        "type": "Фото",
                        "params": photos
                    },
                    {
                        "type": "Фото360",
                        "params": []
                    },
                    {
                        "type": "Видео",
                        "params": []
                    }
                ]
            }
        ]
