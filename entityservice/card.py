from requestsevice import ApiRequest, ErrorResponce
from .exception import CardError


class Card:
    @staticmethod
    def findByBarcodes(barcodes, withError=False, offset=0):
        request = ApiRequest()
        url = 'https://suppliers-api.wildberries.ru/card/list'
        data = {
            "filter": {
                "find": [
                    {
                        "column": "nomenclatures.variations.barcode",
                        "search": barcodes
                    }
                ],
                "order": {
                    "column": "createdAt",
                    "order": "asc"
                }
            },
            "query": {
                "limit": len(barcodes),
                "offset": offset
            },
            "withError": withError
        }
        result = request.request(url, data=data)
        return result.getData().get('cards')


    @staticmethod
    def findByArticule(vendorCode, withError=False, offset=0):
        request = ApiRequest()
        url = 'https://suppliers-api.wildberries.ru/card/list'
        data = {
            "filter": {
                "find": [
                    {
                        "column": "nomenclatures.vendorCode",
                        "search": vendorCode
                    }
                ],
                "order": {
                    "column": "createdAt",
                    "order": "asc"
                }
            },
            "query": {
                "limit": 1,
                "offset": offset
            },
            "withError": withError
        }
        result = request.request(url, data=data)
        return result.getData().get('cards')

    @staticmethod
    def createCard(card_data):
        request = ApiRequest()
        url = 'https://suppliers-api.wildberries.ru/card/create'
        data = {
            "card": card_data
        }
        result = request.request(url, data=data)
        if isinstance(result, ErrorResponce):
            raise CardError(result.getData())
        return result.getData()

    @staticmethod
    def updateCard(card_data):
        request = ApiRequest()
        url = 'https://suppliers-api.wildberries.ru/card/update'
        data = {
            "card": card_data
        }
        result = request.request(url, data=data)
        if isinstance(result, ErrorResponce):
            raise CardError(result.getData())
        return result.getData()

    @staticmethod
    def createCardBatch(card_data_list):
        request = ApiRequest()
        url = 'https://suppliers-api.wildberries.ru/card​/batchCreate'
        data = {
            "card": card_data_list
        }
        result = request.request(url, data=data)
        return result.getData()


    @staticmethod
    def setPrice(price):
        request = ApiRequest()
        url = 'https://suppliers-api.wildberries.ru/public/api/v1/prices'
        data = price
        result = request.request(url, data=data, isWrap=False)
        if isinstance(result, ErrorResponce):
            raise CardError(result.getData())
        return result.getData()

