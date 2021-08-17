from dictservice import DictService


# Бренд
def set_brand(result_data, data):
    params = data.get('categori_props').keys()
    brands_dict = DictService.getDict('brands')
    if params and ('Бренд' in params):
        if brands_dict.get(data.get('vendor')):
            brand_value = brands_dict.get(data.get('vendor'))
            data['brand'] = brand_value
            result_data['addin'].append({
                'type': "Бренд",
                'params': [
                    {
                        "value": brand_value
                    }
                ]
            })
