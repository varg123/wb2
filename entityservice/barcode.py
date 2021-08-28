from requestsevice import ApiRequest


class Barcode:
    _url = 'https://suppliers-api.wildberries.ru/card/getBarcodes'
    _method = 'post'

    __instance = None
    _length = None
    _barcodes = []

    @staticmethod
    def get_barcode():
        data = {
            "quantity": 1
        }
        request = ApiRequest()
        result = request.request(Barcode._url, Barcode._method, data=data)
        return result.getData().get('barcodes')[0]

    @staticmethod
    def get_barcodes(count):
        data = {
            "quantity": count
        }
        request = ApiRequest()
        result = request.request(Barcode._url, Barcode._method, data=data)
        return result.getData().get('barcodes')

    def __init__(self, length=10):
        if not Barcode.__instance:
            self._barcodes = Barcode.get_barcodes(length)
            self._length = len(self._barcodes)
            Barcode.__instance = self

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Barcode()
        return cls.__instance

    def get(self):
        self._upload()
        return self._barcodes[len(self._barcodes) - 1]

    def pop(self):
        self._upload()
        return self._barcodes.pop()

    def _upload(self):
        if len(self._barcodes) == 0:
            self._barcodes = self.get_barcodes(self._length)
