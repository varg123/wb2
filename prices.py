from applog import AppLog

from parserservice import Offers
from dbservice import DbSevice
from entityservice import Card


def main():
    offers = Offers()
    dbservice = DbSevice()
    log = AppLog()
    a = []
    for offer_i in range(offers.getCount()):
        try:
            offer_data = offers.getData()
            if not offer_data.get('id'):
                continue
            id = offer_data.get('id')
            if not offer_data.get('price'):
                continue
            if not dbservice.get(id):
                continue
            if not dbservice.get(id).get('nmId'):
                continue
            nmId = dbservice.get(id).get('nmId')
            price = offer_data.get('price')
            a.append({"nmId": int(nmId), "price": int(int(price) * 1.15)})
        except BaseException as e:
            log.exception(e)


if __name__ == '__main__':
    main()
