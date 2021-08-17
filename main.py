import appconfig
import applog


def main():
    log = applog.AppLog()
    log.error('test')
    try:
        raise ValueError('Test exception')
    except ValueError as e:
        log.exception(e)
    log.product_error(123, 'test')
    log.product_info(12, 'загружен')


if __name__ == '__main__':
    main()
