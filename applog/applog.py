import os
import logging
import json


class AppLog:
    _log_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'log.log')
    _log_products_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'products.json')
    __instance = None
    _products_data = {}
    _is_info = False

    def __init__(self):
        if not AppLog.__instance:
            logging.basicConfig(filename=self._log_path, level=logging.ERROR, filemode='w')
            AppLog.__instance = self

    @classmethod
    def error(cls, text, isExit=False):
        logging.error(text)
        if isExit:
            exit()

    @classmethod
    def exception(cls, e, isExit=False):
        logger = logging.getLogger(__name__)
        logger.exception(e)
        if isExit:
            exit()

    @classmethod
    def product_error(cls, id, text):
        cls.__instance._products_data[id] = {
            'status': 'error',
            'msg': text
        }
        cls.__instance._save()

    @classmethod
    def enableInfo(cls, enable=False):
        cls.__instance._is_info = enable

    @classmethod
    def product_info(cls, id, text):
        if cls.__instance._is_info:
            cls.__instance._products_data[id] = {
                'status': 'success',
                'msg': text
            }
            cls.__instance._save()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = AppLog()
        return cls.__instance

    def _save(self):
        with open(self._log_products_path, 'wt', encoding='utf-8') as config_json:
            json.dump(self._products_data, config_json, ensure_ascii=False)
