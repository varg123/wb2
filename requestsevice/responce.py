class BaseResponce:
    _resp = None

    def __init__(self, resp):
        self._resp = resp

    def getData(self):
        return self._resp.text


class ErrorResponce(BaseResponce):
    def getData(self):
        json_result = self._resp.json()
        if json_result.get('errorText'):
            return json_result

        if json_result.get('error').get('message'):
            return json_result.get('error').get('message')
        return 'Ошибка обработки результата'


class ResultResponce(BaseResponce):
    def getData(self):
        return self._resp.json().get('result')


class ResultCatalogResponce(BaseResponce):
    def getData(self):
        return self._resp.json().get('data')
