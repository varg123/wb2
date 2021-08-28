import os
import json


class DbSevice:
    _products_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'products.json')
    __instance = None
    _products_data = {}
    _is_info = False

    def __init__(self):
        if not DbSevice.__instance:
            with open(self._products_path, 'rt', encoding='utf-8') as config_json:
                self._products_data = json.load(config_json)
            DbSevice.__instance = self

    @classmethod
    def set(cls, id, data):
        cls.__instance._products_data.update({id: data})
        cls.__instance._save()

    @classmethod
    def get(cls, id):
        return cls.__instance._products_data.get(id)

    @classmethod
    def delete(cls, id):
        val = cls.__instance._products_data.get(id)
        if val:
            cls.__instance._products_data.pop(id)
        cls.__instance._save()

    @classmethod
    def keys(cls):
        return cls.__instance._products_data.keys()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DbSevice()
        return cls.__instance

    def _save(self):
        with open(self._products_path, 'wt', encoding='utf-8') as config_json:
            json.dump(self._products_data, config_json, ensure_ascii=False)
