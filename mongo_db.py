from pymongo import MongoClient
import json

# сокрытие данных блок в дальнейшем через config.get
import configparser
config = configparser.ConfigParser()
config.read('config/config.ini', encoding='utf-8-sig')


def get_database():
    CONNECTION_STRING = config.get('database', 'connecting_str')
    client = MongoClient(CONNECTION_STRING)
    return client['API_course_money']

# Подключаемся к нашей базе данных
dbname = get_database()
# Подключаемся к нашей коллекции в базе данных - курс доллар-рубль
collection_name = dbname["usd_rubl"]

# готовим данные для записи в коллекцию
item_1 = {
  "item_name" : "Stimul",
  "max_discount" : "20%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

# выполняем импорт данных
collection_name.insert_one(item_1)