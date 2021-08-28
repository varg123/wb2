from applog import AppLog

from parserservice import Offers
from dbservice import DbSevice
from entityservice import Barcode, Card, Catalog
from handlerservice import HService, default_update_list, default_add_list
from excelservice import RemainsService
from entityservice import Remains


def main():
    offers = Offers()
    dbservice = DbSevice()
    remains = RemainsService()
    log = AppLog()
    for offer_i in range(offers.getCount()):
        offer_data = offers.getData()
        try:
            db_info = dbservice.get(offer_data.get('id'))
            if offer_data.get('vendor') == '':
                continue
            if db_info is None:
                continue
            barcode = db_info.get('barcode')
            isLoad = not db_info.get('isNotRemain')
            outlet = offer_data.get('outlet')
            if None not in [barcode, outlet]:
                if isLoad:
                    remains.set(barcode, outlet)
        except BaseException as e:
            log.exception(e)
    remains.save()
    Remains.upload(remains.getPath())


if __name__ == '__main__':
    main()
