
FROM python:3.11

WORKDIR /code

RUN mkdir app

COPY ./requirements.txt /code/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/app/requirements.txt

COPY ./crawler /code/app/crawler
COPY ./rest-api /code/app/rest-api

RUN pip install --no-cache-dir --upgrade -r /code/app/rest-api/requirements.txt

RUN export PYTHONPATH=$PWD

CMD ["uvicorn", "app.rest-api.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]