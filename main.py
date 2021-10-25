import re

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
    barcodeservice = Barcode()
    updateservice = HService(default_update_list)
    createservice = HService(default_add_list)
    remains = RemainsService()
    log = AppLog()
    for offer_i in range(offers.getCount()):
        offer_data = offers.getData()
        print(f'{offer_i + 1}/{offers.getCount()} - {offer_data}')
        try:
            db_info = dbservice.get(offer_data.get('id'))
            if db_info is None:
                db_info = {}
            is_hash_falied = True
            if db_info.get('hash') == offer_data.get('hash'):
                is_hash_falied = False

            # TODO:удалить
            is_hash_falied = True

            find_offer_data = {}

            # поиск по баркоду если есть в базе
            barcode = db_info.get('barcode')
            if is_hash_falied and not find_offer_data and barcode:
                find_cards = Card.findByBarcodes([barcode])
                if find_cards:
                    find_offer_data = find_cards.pop()

            reg = re.compile('[\sё]|(&[a-z]*;)')
            articul = reg.sub('_', offer_data.get('param').get('Код товара'))[:35]
            if is_hash_falied and not find_offer_data and articul:
                find_cards = Card.findByArticule(articul)
                if find_cards:
                    find_offer_data = find_cards.pop()

            if find_offer_data:
                updateservice.apply(offer_data, find_offer_data)

            if find_offer_data:
                Card.updateCard(find_offer_data)

            if find_offer_data:
                if find_offer_data.get('nomenclatures'):
                    db_info['nmId'] = find_offer_data.get('nomenclatures')[0].get('nmId')
                if find_offer_data.get('nomenclatures'):
                    variations = find_offer_data.get('nomenclatures')[0].get('variations')
                    if variations:
                        db_info['barcode'] = \
                            find_offer_data.get('nomenclatures')[0].get('variations')[0].get('barcodes')[0]

            create_offer_data = {}
            if is_hash_falied and not find_offer_data:
                createservice.apply(offer_data, create_offer_data)
            if create_offer_data:
                Card.createCard(create_offer_data)

            if create_offer_data:
                barcode = barcodeservice.get()
                db_info['barcode'] = barcode
                barcodeservice.pop()

            exception_remains_brands = [
                # 'ADRIATICA',
                # 'CITIZEN',
                # 'EPOS',
                # 'PIERRE RICAUD',
                # 'RAYMOND WEIL',
                # 'SWISS MILITARY HANOW',
                # 'NAUTICA',
                # 'ANNE KLEIN',
            ]

            if db_info.get('hash') != offer_data.get('hash'):
                db_info['hash'] = offer_data.get('hash')

            if offer_data.get('vendor') in exception_remains_brands:
                db_info['isNotRemain'] = True
            dbservice.set(offer_data.get('id'), db_info)
            if not db_info.get('isNotRemain'):
                remains.set(db_info['barcode'], offer_data.get('outlet'))
        except BaseException as e:
            log.product_error(offer_data.get('id'), str(e))
            log.exception(e)
    remains.save()
    Remains.upload(remains.getPath())




if __name__ == '__main__':
    main()
