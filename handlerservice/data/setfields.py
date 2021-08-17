#todo:перенести в другой раздел
def sub_setfields(result_data, data):
    categori = data.get('object')
    config = BaseConfig()
    res = CatalogsRequest(config).get_translated(categori)
    res_props = res.getData().get('addin')
    data['categori_props'] = {}
    if res_props:
        for prop in res_props:
            data['categori_props'][prop['type']] = prop