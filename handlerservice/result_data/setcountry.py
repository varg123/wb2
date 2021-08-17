from dictservice import DictService


# Страна countryProduction
def set_country(result_data, data):
    countries = DictService.getDict('countries')
    default_country = countries.get('default')
    countries_dict = countries.get('data')
    vendor = data.get('vendor')
    if vendor:
        if countries_dict.get(vendor):
            result_data['countryProduction'] = countries_dict.get(vendor)
            return data
    result_data['countryProduction'] = default_country
