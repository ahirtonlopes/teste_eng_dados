from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os
from pathlib import Path
from dotenv import load_dotenv

# Enviroment Variables
load_dotenv()
BUCKET_PATH=os.getenv('BUCKET_PATH')
JSON_PATH=os.getenv('JSON_PATH')
JSON_FILE = str(Path(JSON_PATH,'data.json'))

if __name__ == '__main__':
  spark = SparkSession.builder\
          .master("local")\
          .appName("Colab")\
          .config('spark.ui.port', '4050')\
          .getOrCreate()

  # le arquivo json
  df_json = spark.read.option("multiline",True).json(JSON_FILE)

  # Explode Campo ItemLista 
  df_json = df_json.select('*',
                               F.posexplode("ItemList")\
                              .alias("ProductCode","Products"))

  # Gera dataframe de produtos de nota fiscal
  df_nota_fiscal_produtos = df_json\
                  .select('NFeNumber','ProductCode','Products')\
                  .withColumn('ProductKey',F.concat(df_json['NFeNumber'],df_json['ProductCode']))\
                  .withColumn('ProductName',df_json['Products']['ProductName'])\
                  .withColumn('Quantity',df_json['Products']['Quantity'])\
                  .withColumn('Value',df_json['Products']['Value'])\
                  .drop(*(['NFeNumber','ProductCode','Products']))
  
  df_nota_fiscal_produtos.show()

  # Gera dataframe de nota fiscal
  df_nota_fiscal = df_json\
                    .withColumn('ProductKey',F.concat(df_json['NFeNumber'],df_json['ProductCode']))\
                    .drop(*(['Products','ProductCode','ItemList']))
  
  df_nota_fiscal.show()