import re


# Код товара (+в номенклатуре), Артикул поставщика
def set_kod_tovara(result_data, data):
    reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
    str_kod = ''
    # if data.get('brand'):
    #     str_kod += data.get('brand')
    if data.get('id'):
        str_kod = data.get('id')
    result_data['supplierVendorCode'] = str_kod
