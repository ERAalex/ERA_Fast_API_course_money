import requests
from pprint import pprint
# библиотека для парсинга XML
import xmltodict as xmltodict


class Api_coin():
    def __init__(self, name_coin:str, date:str):
        self.name_coin = name_coin
        self.date = date

    # сделаем статик метод, чтобы в нем загрузить логику извлечения нужной информации и не повторять код в дальнейшем
    # don't repeat yourself
    @staticmethod
    def parser_coins(result_of_parse, name_coin):
        data_coins = []


        for item, value in result_of_parse.items():
            for item1, value1 in value.items():
                data_coins = value1

        result_diccionary = {}
        for item in data_coins:
            for key, value in item.items():
                if value == name_coin:
                    result_diccionary['Name_coin'] = item['Name']
                    result_diccionary['CharCode'] = item['CharCode']
                    result_diccionary['Value'] = item['Value']
                    result_diccionary['Nominal'] = item['Nominal']

        return result_diccionary


    # запрос выдает стоимость 1 валюты к рублю
    def check_coin_today(self):
        url_rub_each_coin = 'http://www.cbr.ru/scripts/XML_daily.asp'

        response = requests.get(url_rub_each_coin)
        result = xmltodict.parse(response.content)

        # передаем значения в статик метод для получения данных по монете
        result_diccionary = self.parser_coins(result, self.name_coin)

        return result_diccionary



    # запрос выдает стоимость 1 валюты к рублю
    def check_coin_some_date(self):
        url_rub_coin_by_date = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={self.date}'

        response = requests.get(url_rub_coin_by_date)
        result = xmltodict.parse(response.content)

        # передаем значения в статик метод для получения данных по монете
        result_diccionary = self.parser_coins(result, self.name_coin)

        return result_diccionary


# see_coin = Api_coin('GBP', '12.07.2015')

# print(see_coin.check_coin_today())
# see_coin.check_coin_some_date()