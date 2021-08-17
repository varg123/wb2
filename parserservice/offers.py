import xml.etree.cElementTree as ET
import requests
from zlib import crc32
from appconfig import AppConfig
import os

download_url = 'https://6624.su/administrator/components/com_excel2vm/models/yml_export.php?profile=wildberries'
xml_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.xml')


# todo: сделать итератор
class Offers:
    _file_path = None
    _data = []
    _i = 0

    def __init__(self):
        self._download_file()
        self._file_path = xml_path
        self._data = self._get_offers_data()

    def _get_node_val(self, tree, dict, name):
        val = tree.find(name)
        if val is not None:
            dict[name] = val.text

    # def getCount(self):
    #     return len(self._data)
    #
    # def getIter(self):
    #     return self._i

    def getData(self):
        self._i += 1
        for it in self._data:
            yield it

    def _get_offers_data(self):
        tree = ET.parse(self._file_path)
        categories = tree.findall('shop/categories/category')
        categories_dict = {}
        for element in categories:
            categories_dict[element.get('id')] = element.text
        offers_list = []
        offers = tree.findall('shop/offers/offer')
        for offer in offers:
            pictures = []
            for picture in offer.findall('picture'):
                pictures.append(picture.text)

            params = {}
            for param in offer.findall('param'):
                params[param.get('name')] = param.text

            offer_dict = {
                'id': offer.get('id'),
                'price': offer.find('price').text,
                'category': categories_dict[offer.find('categoryId').text],
                'name': offer.find('name').text,
                'vendor': offer.find('vendor').text,
                'typePrefix': offer.find('typePrefix').text,
                'picture': pictures,
                'vat': offer.find('vat').text,
                'param': params,
            }
            self._get_node_val(offer, offer_dict, 'description')
            self._get_node_val(offer, offer_dict, 'dimensions')
            self._get_node_val(offer, offer_dict, 'width')
            self._get_node_val(offer, offer_dict, 'sales_notes')
            self._get_node_val(offer, offer_dict, 'weight')
            self._get_node_val(offer, offer_dict, 'length')
            self._get_node_val(offer, offer_dict, 'height')
            self._get_node_val(offer, offer_dict, 'outlet')

            offers_list.append(offer_dict)
        return offers_list

    def _download_file(self):
        s = requests.Session()
        res = s.get(download_url)
        configApp = AppConfig()
        if configApp.get('hash_xml') == crc32(res.content):
            return
        configApp.set('hash_xml', crc32(res.content))
        with open(xml_path, 'wt', encoding='utf-8') as file:
            file.write(res.text)
