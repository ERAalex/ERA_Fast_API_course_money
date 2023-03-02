from fastapi import FastAPI
from starlette.responses import JSONResponse
import json

from api_request_cbr import Api_coin
from mongo_db import Mongo_db_connect
from fastapi.encoders import jsonable_encoder
import datetime
date = datetime.datetime.now()

app = FastAPI(
    title='Testing Server Espinosa'
)

# start local server on Fast Api - uvicorn main:app --reload

# название функции будет отображено в описании документации. Подбирай название
@app.get('/')
def hello():
    return "Hello World"


@app.get('/coin/{coin}')
def get_coin_course(coin: str):
    date_now = date.strftime('%d.%m.20%y')

    # ищем в базе данные, в Mongo. Если не будет в базе, сразу внутри нее создасть запрос к API sber подтянет данные и
    # запишет в базу.
    check_coin = Mongo_db_connect()
    result = check_coin.check_exist_date_if_none_create(coin, date_now)

    # есть проблема, что FastApi не может перевести  Object_id из Mongo в JSON, т.к. это
    # сущность, а не просто строка или число. поэтому нам надо убрать его(выкинем) в самой функции где у нас работа с БД


    return result


@app.get('/coin/{coin}/{date}')
def get_coin_course_date(coin: str, date: str):

    # ищем в базе данные, в Mongo. Если не будет в базе, сразу внутри нее создасть запрос к API sber подтянет данные и
    # запишет в базу.
    check_coin = Mongo_db_connect()
    result = check_coin.check_exist_date_if_none_create(coin, date)

    # на выходе мы получаем словарь, но передать нам нужно JSON поэтому надо конвертировать данные
    result_json = jsonable_encoder(result)

    return result_json