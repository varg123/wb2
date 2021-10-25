import json
import xml.etree.cElementTree as ET
import requests
from zlib import crc32
from appconfig import AppConfig
import os

download_url = 'https://6624.su/1c_unload/market_2.xml'
xml_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.xml')


# todo: сделать итератор
class Offers:
    _file_path = None
    _data = []
    _i = 0

    def __init__(self):
        # self._download_file()
        self._file_path = xml_path
        self._i = 0
        self._data = self._get_offers_data()

    def _get_node_val(self, tree, dict, name):
        val = tree.find(name)
        if val is not None:
            dict[name] = val.text

    def getCount(self):
        return len(self._data)

    def getIter(self):
        return self._i

    def getData(self):
        data = self._data[self._i]
        self._i += 1
        return data

    def _get_offers_data(self):
        tree = ET.parse(self._file_path)
        categories = tree.findall('shop/categories/category')
        categories_dict = {}
        for element in categories:
            categories_dict[element.get('id')] = element.text
        offers_list = []
        offers = tree.findall('shop/offers/offer')
        # with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'products.json'), 'rt', encoding='utf-8') as file:
        #     ids = json.load(file).keys()
        for offer in offers:
            # if offer.get('id') != '107090':# not in ids:_
            #     continue
            hash_fields = ''
            pictures = []
            for picture in offer.findall('picture'):
                pictures.append(picture.text)
                hash_fields += picture.text

            params = {}
            for param in offer.findall('param'):
                params[param.get('name')] = param.text
                hash_fields += param.text

            if offer.find('vendor').text == 'DKNY':
                continue
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
            hash_fields += offer.find('name').text
            hash_fields += offer.find('vat').text
            offer_dict['hash'] = crc32(hash_fields.encode('utf-8'))
            self._get_node_val(offer, offer_dict, 'description')
            self._get_node_val(offer, offer_dict, 'dimensions')
            self._get_node_val(offer, offer_dict, 'width')
            self._get_node_val(offer, offer_dict, 'sales_notes')
            self._get_node_val(offer, offer_dict, 'weight')
            self._get_node_val(offer, offer_dict, 'length')
            self._get_node_val(offer, offer_dict, 'height')
            self._get_node_val(offer, offer_dict, 'outlet')

            # todo: удвлить условия фильтрации
            # if offer_dict.get('id') != '106989':
            #     continue

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
