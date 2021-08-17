import os
import json

class DictService:
    _dicts_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dictionaries')

    @classmethod
    def getDict(cls, name):
        file_path = os.path.join(cls._dicts_path, f'{name}.json')
        with open(file_path, 'rt', encoding='utf-8') as file:
            return json.load(file)

