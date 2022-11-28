from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os
from pathlib import Path
from dotenv import load_dotenv

# Enviroment Variables
load_dotenv()
BUCKET_PATH=os.getenv('BUCKET_PATH')
ARQUIVOS_CSV = ['contrato.csv','cliente.csv','transacao.csv']

if __name__ == '__main__':
  spark = SparkSession.builder\
          .master("local")\
          .appName("Colab")\
          .config('spark.ui.port', '4050')\
          .getOrCreate()

  # le arquivos csv
  try:
    [df_contrato , df_cliente, df_transacao ] = [ spark.read.options(header=True, delimiter=";").csv(str(Path(BUCKET_PATH,csv))) for csv in ARQUIVOS_CSV ]
  except:
    os.sys(1)
    print("Erro ao ler arquivos csvs")

  # trata campos nulos
  df_transacao = df_transacao.fillna({'percentual_desconto':0, 'valor_total':0})

  # calcula valor liquido
  df_transacao_taxa = df_transacao.withColumn("vlr_liquido", df_transacao['valor_total'] - (df_transacao['valor_total'] * df_transacao['percentual_desconto']/100))\
                            .drop(*(['percentual_desconto','valor_total']))

  df_result = df_transacao_taxa.join(df_contrato,['contrato_id'])\
                .join(df_cliente,df_cliente['cliente_id'] == df_contrato['cliente_id'])\
                .withColumn("tx_administrativa", df_transacao_taxa['vlr_liquido'] * df_contrato['percentual']/100)\
                .where(df_contrato['ativo'] == 1)\
                .groupBy(df_cliente['nome']).sum('tx_administrativa')              

  df_result.show()