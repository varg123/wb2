from requestsevice import CatalogRequest


class Catalog:
    @staticmethod
    def get_object(pattern):
        req = CatalogRequest()
        params = {
            'pattern': pattern,
            'lang': 'ru'
        }
        url = 'https://content-suppliers.wildberries.ru/ns/characteristics-configurator-api/content-configurator/api/v1/config/get/object/list'
        res = req.request(url, 'get', params=params)
        return res.getData()

    @staticmethod
    def get_directories():
        req = CatalogRequest()
        url = 'https://content-suppliers.wildberries.ru/ns/characteristics-configurator-api/content-configurator/api/v1/directory/get/list'
        res = req.request(url, 'get')
        return res.getData()

    @staticmethod
    def get_tnved(subject):
        req = CatalogRequest()
        params = {
            'subject': subject
        }
        url = 'https://content-suppliers.wildberries.ru/ns/characteristics-configurator-api/content-configurator/api/v1/directory/tnved'
        res = req.request(url, 'get', params=params)
        return res.getData()

    @staticmethod
    def get_from_directory(directory_name, pattern='', option='', top=10):
        req = CatalogRequest()
        params = {}
        if option:
            params = {
                'option': option,
                'lang': 'ru',
                'top': top

            }
        if pattern:
            params = {
                'pattern': pattern,
                'lang': 'ru',
                'top': top

            }
        url = f'https://content-suppliers.wildberries.ru/ns/characteristics-configurator-api/content-configurator/api/v1/directory/{directory_name}'
        res = req.request(url, 'get', params=params)
        return res.getData()

    @staticmethod
    def get_translated(name):
        req = CatalogRequest()
        params = {
            'name': name,
            'lang': 'ru',

        }
        url = f'https://content-suppliers.wildberries.ru/ns/characteristics-configurator-api/content-configurator/api/v1/config/get/object/translated'
        res = req.request(url, 'get', params=params)
        return res.getData()
