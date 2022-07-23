from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os
from pathlib import Path

# Environment Variables Load
load_dotenv()
BUCKET_PATH=os.getenv('BUCKET_PATH')

# Database Variables
CONNECTOR_TYPE=os.getenv('CONNECTOR_TYPE')
URL = os.getenv('SQLSERV_URL')
SQL_USERNAME=os.getenv('SQL_USERNAME')
SQL_PASSWORD=os.getenv('SQL_PASSWORD')

# Table Name
TABELA = "[desafio_engenheiro].[dbo].[contrato]"
CSV_FILE = "contrato.csv"

if __name__ == "__main__":
    spark = SparkSession.builder\
        .master("local")\
        .appName("Ingestao contrato")\
        .config("spark.sql.")\
        .getOrCreate()

    df = spark.read \
            .format(CONNECTOR_TYPE) \
            .option("url", URL) \
            .option("dbtable", TABELA) \
            .option("user", SQL_USERNAME) \
            .option("password", SQL_PASSWORD).load()

    df.write.csv(str(Path(BUCKET_PATH,CSV_FILE)))
