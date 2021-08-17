from dictservice import DictService


# object
def set_object(result_data, data):
    default_val = DictService.getDict('object').get('default')
    val_dict = DictService.getDict('object').get('data')
    cat = data.get('category')
    if cat:
        if val_dict.get(cat):
            result_data['object'] = val_dict.get(cat)
            data['object'] = val_dict.get(cat)
            return data
    result_data['object'] = default_val
    data['object'] = default_val
