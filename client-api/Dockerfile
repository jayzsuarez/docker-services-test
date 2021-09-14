FROM python:3.7.11-slim-stretch

WORKDIR /home/app

COPY requirements.txt /code
COPY ./app.py /home/app/app.py
COPY ./requirements.txt /home/app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]