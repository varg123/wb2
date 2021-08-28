from appconfig import AppConfig
from requestsevice import LkRequest
import requests
class Remains:
    @staticmethod
    def upload(file_path):
        files = {
            'file': (
                'остатки.xlsx', open(file_path, 'rb'),
                'application/vnd.ms-excel', {'Expires': '0'}
            )
        }
        appconfig = AppConfig.getInstance()
        url = f"https://seller.wildberries.ru/ns/api/suppliers-portal-marketplace/api/v2/portal/stocks/uploads?key={appconfig.get('key')}"
        requests.models.Request()
        req = LkRequest().request(url, files=files, data={'warehouseId': appconfig.get('warehouseId')})
        return req.getData()
