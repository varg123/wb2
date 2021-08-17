import appconfig
import applog
import dictservice
import excelservice
import time
from parserservice import Offers
from requestsevice import BaseRequest, ApiRequest


def main():
    # data = {
    #     "quantity": 10,
    # }
    # res = ApiRequest().request('https://suppliers-api.wildberries.ru/card/getBarcodes', 'post', data=data)

    data = {
        "filter": {
            "find": [
                {
                    "column": "nomenclatures.variations.barcode",
                    "search": ["2006777209002", "2006723300005"]
                }
            ],
            "order": {
                "column": "createdAt",
                "order": "asc"
            }
        },
        "query": {
            "limit": 10
        }
    }
    res = ApiRequest().request('https://suppliers-api.wildberries.ru/card/list', 'post', data=data)
    print(res.getData())
    # offers = Offers()
    # for it in offers.getData():
    #     print(it)
    #     time.sleep(1)

    # balances = excelservice.Remains()
    # balances.set('123', 2)
    # balances.set('234', 1)
    # balances.save()
    # print(balances.getPath())


if __name__ == '__main__':
    main()
