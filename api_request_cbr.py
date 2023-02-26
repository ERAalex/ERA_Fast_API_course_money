import requests
from pprint import pprint
# библиотека для парсинга XML
import xmltodict as xmltodict


class Api_coin():
    def __init__(self, name_coin:str):
        self.name_coin = name_coin

    # запрос выдает стоимость 1 валюты к рублю
    def check_coin_today(self):
        url_rub_each_coin = 'http://www.cbr.ru/scripts/XML_daily.asp'

        response = requests.get(url_rub_each_coin)
        result = xmltodict.parse(response.content)

        data_coins = []

        for item, value in result.items():
            for item1, value1 in value.items():
                data_coins = value1

        pprint(data_coins)
        for item in data_coins:
            for key, value in item.items():
                if value == self.name_coin:
                    print('курс' + ' ' + item['Name'])
                    print(item['Value'])
                    print('за' + ' ' + item['Nominal'] + ' ' + item['CharCode'])


    # запрос выдает стоимость 1 валюты к рублю
    def check_coin_some_date(self):
        url_rub_coin_by_date = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={some_date}'




see_coin = Api_coin('Евро')

see_coin.check_coin_today()