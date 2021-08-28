import requests
from .config import *
from .responce import *
import uuid
import json


class BaseRequest:
    _session = None

    def __init__(self):
        self._session = requests.Session()
        self._config = BaseConfig()

    def request(self, url, method='post', params=None, files=None, headers=None, data=None, cookies=None):
        if params:
            params.update(self._config.get_params())
        elif self._config.get_params():
            params = self._config.get_params()
        if files:
            files.update(self._config.get_files())
        elif self._config.get_files():
            files = self._config.get_files()

        if headers:
            headers.update(self._config.get_headers())
        elif self._config.get_headers():
            headers = self._config.get_headers()

        if isinstance(data, list):
            None
        elif data:
            data.update(self._config.get_data())
        elif self._config.get_data():
            data = self._config.get_data()

        if cookies:
            cookies.update(self._config.get_cookie())
        elif self._config.get_cookie():
            cookies = self._config.get_cookie()

        if not files:
            data = json.dumps(data)
        resp = self._session.request(method, url, params=params, data=data, headers=headers,
                                     cookies=cookies,
                                     files=files)
        return self._get_resp(resp)

    def _get_resp(self, resp):
        return BaseResponce(resp)


class CatalogRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self._session = requests.Session()
        self._config = ApiConfig()

    def request(self, url, method='post', params=None, files=None, headers=None, data=None, cookies=None):
        return super().request(url, method=method, params=params, files=files, headers=headers, data=data,
                               cookies=cookies)

    def _get_resp(self, resp):
        result_json = resp.json()
        if 'data' in result_json:
            return ResultCatalogResponce(resp)
        return BaseResponce(resp)


class ApiRequest(BaseRequest):

    def __init__(self):
        super().__init__()
        self._session = requests.Session()
        self._config = ApiConfig()

    def _wrap_data(self, data):
        return {
            "id": str(uuid.uuid4()),
            "jsonrpc": "2.0",
            "params": data
        }

    def request(self, url, method='post', params=None, files=None, headers=None, data=None, cookies=None, isWrap=True):
        if isWrap:
           data = self._wrap_data(data)
        return super().request(url, method=method, params=params, files=files, headers=headers, data=data,
                               cookies=cookies)

    def _get_resp(self, resp):
        if resp.text:
            result_json = resp.json()
        else:
            result_json = {}
        if 'error' in result_json:
            return ErrorResponce(resp)
        if 'result' in result_json:
            return ResultResponce(resp)
        return BaseResponce(resp)


class LkRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self._config = LkConfig()
