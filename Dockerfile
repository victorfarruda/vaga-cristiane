FROM python:3.8

ADD ./src /src
RUN pip install -r src/requirements.txt

WORKDIR /src
CMD python /src/main_tratamento.py
