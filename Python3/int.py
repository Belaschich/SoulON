import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("Aula Introdutória PySpark") \
    .config("spark.executor.memory", "1gb") \
    .getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("C:\\Users\\izabe\\Documents\\GitHub\\SoulON\\Python3\\Salary_Data.csv")
print("Concluído com sucesso!")