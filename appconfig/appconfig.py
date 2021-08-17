import os
import json


class AppConfig:
    _config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.json')
    _data = {}
    __instance = None

    def __init__(self):
        if not AppConfig.__instance:
            with open(self._config_path, 'rt', encoding='utf-8') as config_json:
                self._data = json.load(config_json)
                AppConfig.__instance = self

    @classmethod
    def get(cls, param):
        return cls.__instance._data.get(param)

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = AppConfig()
        return cls.__instance
