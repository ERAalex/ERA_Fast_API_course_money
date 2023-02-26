from fastapi import FastAPI

import configparser
config = configparser.ConfigParser()
config.read('config/config.ini', encoding='utf-8-sig')


app = FastAPI(
    title='Testing Server Espinosa'
)


# название функции будет отображено в описании документации. Подбирай название
@app.get('/')
def hello():
    return "Hello Worldss"


