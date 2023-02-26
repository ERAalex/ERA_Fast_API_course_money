from fastapi import FastAPI

app = FastAPI(
    title='Testing Server Espinosa'
)


# название функции будет отображено в описании документации. Подбирай название
@app.get('/')
def hello():
    return "Hello Worldss"


