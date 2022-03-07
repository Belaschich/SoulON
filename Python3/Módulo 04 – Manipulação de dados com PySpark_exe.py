from pyspark.sql.session import SparkSession

from pyspark.sql.types import (ArrayType, BooleanType, FloatType, IntegerType, StringType, StructField, StructType, TimestampType, DoubleType)

import pyspark.sql.functions as F

spark = SparkSession.builder.appName('fisrtSession')\
    .config('spark.master', 'local[4]')\
    .config('spark.executor.memory', '1gb')\
    .config('spark.shuffle.partitions', 1)\
    .getOrCreate()

schema = StructType([
      StructField("ID",IntegerType()),
      StructField("Idade",IntegerType()),
      StructField("Trabalho",StringType()),
      StructField("ZipCode",IntegerType()),
      StructField("Educacao",StringType()),
      StructField("Numero_Educacao",IntegerType()),
      StructField("Status_relacionamento",StringType()),
      StructField("Profissão",StringType()),
      StructField("Relacionamento",StringType()),
      StructField("Raca",StringType()),
      StructField("Sexo",StringType()),
      StructField("hr_semana",IntegerType()),
      StructField("País",StringType()),
      StructField("salario",DoubleType())
  ])

path = ("C:/Users/izabe/Documents/GitHub/SoulON/Python3/adult_data.csv")

df = spark.read.format('csv')\
    .schema(schema)\
    .load(path)

df.printSchema()

df.show(5)

def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe

colunas = ['Idade']

df = converterColuna(df, colunas, FloatType())

df.show()

df2 = df.select('Idade', 'Educacao')

df2.show(5)

df3 = df.sort(F.desc('Educacao'))

df3.show()

df.describe('salario').show()

spark.stop()


