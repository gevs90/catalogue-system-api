FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install psycopg2-binary
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip3 install --editable .

COPY ./app /code/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
