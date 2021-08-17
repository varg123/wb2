from appconfig import AppConfig


class BaseConfig:
    _appconfig = AppConfig()

    def get_params(self):
        return {}

    def get_data(self):
        return {}

    def get_files(self):
        return {}

    def get_headers(self):
        return {}

    def get_cookie(self):
        return {}


class ApiConfig(BaseConfig):
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': self._appconfig.get('token'),
        }


class LkConfig(BaseConfig):
    def get_headers(self):
        return {
            'Authorization': self._appconfig.get('token'),
        }

    def get_cookie(self):
        return {
            'WBToken': self._appconfig.get('WBToken'),
            "x-supplier-id": self._appconfig.get('x-supplier-id'),
        }

    def get_params(self):
        return {
            'key': self._appconfig.get('key')
        }
