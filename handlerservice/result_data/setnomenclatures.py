import re
from entityservice import Barcode


# todo: добавить баркоды, добавить проверку битых фото
# Номенклатура Розничная цена Фото
def set_nomenclatures(result_data, data):
    photos = []
    for pict in data.get('picture'):
        photos.append({
            'value': pict
        })
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
        reg = re.compile('[\sё]|(&[a-z]*;)')
        data['barcode'] = result_data['nomenclatures'][0]['variations'][0]['barcodes'][0]
        data['barcode'] = result_data['nomenclatures'][0]['vendorCode'] = reg.sub('_', data.get('param').get('Код товара'))[:35]
    else:
        barcode = Barcode.getInstance().get()
        data['barcode'] = barcode

        reg = re.compile('[\sё]|(&[a-z]*;)')
        result_data['nomenclatures'] = [
            {

                "vendorCode": reg.sub('_', data.get('param').get('Код товара'))[:35],
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
