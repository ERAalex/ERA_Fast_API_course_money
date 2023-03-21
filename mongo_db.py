from pymongo import MongoClient
import json
from api_request_cbr import Api_coin

# сокрытие данных блок в дальнейшем через config.get
import configparser
config = configparser.ConfigParser()
config.read('config/config.ini', encoding='utf-8-sig')


class Mongo_db_connect():
    def __init__(self):
        # self.CONNECTION_STRING = config.get('database', 'connecting_str')
        # self.CONNECTION_STRING = 'mongodb://127.0.0.1:27017'
        self.CONNECTION_STRING = 'mongodb://root:nazca007@mongo:27017/'
        self.client = MongoClient(self.CONNECTION_STRING)
        self.dbname = self.client['API_course_money']
        self.collection_name = self.dbname['usd_rubl']

    def create_new_collection(self, coin: str, date: str, diccionary_value: dict):
        collection_name = self.dbname[f'{coin}_rubl']

        result = collection_name.insert_one(
            {
                "date": f'{date}',
                "Name_coin": f"{diccionary_value['Name_coin']}",
                "CharCode": f"{diccionary_value['CharCode']}",
                "Value": f"{diccionary_value['Value']}",
                "Nominal": f"{diccionary_value['Nominal']}",
            })

        # {'_id': 0} - выкидываем поле с ID тк это сущность и нам ее не передать в JSON в API
        result = collection_name.find_one({'date': f'{date}'}, {'_id': 0})

        return result

    def check_exist_date_if_none_create(self, coin, date):

        # ищем в базе по дате и по нужной коллекции
        collection_name = self.dbname[f'{coin}_rubl']
        # {'_id': 0} - выкидываем поле с ID тк это сущность и нам ее не передать в JSON в API
        find_item = collection_name.find_one({'date': f'{date}'}, {'_id': 0})

        # если инофрмация не была найдена, то делаем Api запрос к банку и получаем словарь через класс Api_coin
        if find_item == None:
            new_coin = Api_coin(coin, date)
            result_dicc = new_coin.check_coin_some_date()

            # передаем словарь в функцию по записи в базу данных (она выше)
            result = self.create_new_collection(coin, date, result_dicc)

            return result
        else:
            return find_item


# check_base = Mongo_db_connect()
# check_base.check_exist_date_if_none_create('UAH', '01.02.2013')
# check_exist_date_if_none_create('Евро', '12.07.2021')

