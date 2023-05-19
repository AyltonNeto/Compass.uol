FROM python:3.10-slim

COPY . .

WORKDIR /app

RUN pip install boto3

CMD python desafio_ETL.py

'Obs: Os arquivos movies.csv e series.csv devem estar na pasta /app'