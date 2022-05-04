FROM python:3.9.11

RUN mkdir app
COPY . ./app/
WORKDIR ./app

RUN pip install kafka-python
CMD ["python", "producer.py"]