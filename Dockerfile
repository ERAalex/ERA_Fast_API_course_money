# собираем образ программы Money APIs
FROM python:3.9

COPY . /src

COPY ./requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

EXPOSE 6060

WORKDIR src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6060"]