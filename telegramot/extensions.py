import json
import requests
from configi import valut

class ApiException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(values):

        if len(values) != 3:
            raise ApiException('Неверное количество параметров!')
        quote, base, amount = values

        if amount == 0:
            raise ApiException('Нулевое количество переводимой валюты')

        if quote == base:
            raise ApiException(f'Невозможно перевести одинаковые валюты! {base}')

        try:
            quote_format = valut[quote]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {quote}')

        try:
            base_format = valut[base]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_format}&symbols={base_format}')

        total = float(json.loads(r.content)['rates'][base_format]) * amount

        return round(total, 3)