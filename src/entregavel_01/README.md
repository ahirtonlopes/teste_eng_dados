# Diário de Solução

## Preparação do ambiente Desenvolvimento 
### Pyspark 
Optei por instalar na máquina
- baixar winutils 
- baixar hadoop-spark 
- Setar variaveis de ambiente
- Baixar conector sql server jar
- Copiar para pasta spark-hadoop/jars/

### Sql Server
Sql Server instala muita coisa na máquina, então optei pelo docker
```shell
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=#sa123456" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest
```

## Execução do exercício
Contexto: Como solução foi criado um mini data lake, isso implica em primeiramente a ingestão 
dos dados na camada raw (as is). Escolhi o formato csv pela simplicidade, mas o ideal em se tratando de gcp seria avro ou parquet.
Após a ingestão consumir os dados

## Fluxo de Carga
1- Ingestão das tabelas na camada raw (pyspark_load_clientes.py - pyspark_load_contrato.py - pyspark_load_transacao)
2- Efetuar calculo com base nas tabelas da camada raw ()

## Pontos de melhoraria
- Passaria a senha criptografada do banco
- Efetuaria a ingestão da camada raw pelo dataflow (Apache Beam)
- Se o custo não for um problema construir a camada raw no bigquery 
- E calculo pelo bigquery
- Orquestração via composer (airflow)