from fastapi import FastAPI
from api_request_cbr import Api_coin

app = FastAPI(
    title='Testing Server Espinosa'
)


# название функции будет отображено в описании документации. Подбирай название
@app.get('/')
def hello():
    return "Hello World"


@app.get('/coin/{coin}')
def get_coin_course(coin:str):
    check_coin = Api_coin(coin, 'some_date')
    result = check_coin.check_coin_today()

    return result


@app.get('/coin/{coin}/{date}')
def get_coin_course_date(coin:str, date:str):
    check_coin = Api_coin(coin, date)
    result = check_coin.check_coin_some_date()

    return result