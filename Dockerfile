FROM python:3.8

WORKDIR /django_celery

ENV PYTHONUNBUFFERED 1

COPY req.txt req.txt

RUN pip install -r req.txt


COPY . .
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]