from entityservice import Catalog


def set_fields(result_data, data):
    categori = data.get('object')
    res = Catalog.get_translated(categori)
    res_props = res.get('addin')
    data['categori_props'] = {}
    if res_props:
        for prop in res_props:
            data['categori_props'][prop['type']] = prop
