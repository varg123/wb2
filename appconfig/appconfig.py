# todo: сделать сингтон чтобы убрать постоянную загрузку словаря

import os
import json


class AppConfig:
    _config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.json')
    _data = {}

    def __init__(self):
        with open(self._config_path, 'rt', encoding='utf-8') as config_json:
            self._data = json.load(config_json)

    def get(self, param):
        return self._data.get(param)
