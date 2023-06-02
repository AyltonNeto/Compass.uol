from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
import pyspark.sql.functions as func

spark = SparkSession \
                .builder \
                .master("local[*]")\
                .appName("Exercicio Intro") \
                .getOrCreate()

# Etapa 1
df_nomes = spark.read.csv("C:/Programação/Projetos/Compass.uol/Sprint08/.DataAnalytics08/Tarefa03/nomes_aleatorios.txt")
df_nomes.show(5)

# Etapa 2
df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")
df_nomes.printSchema()
df_nomes.show(10)

# Etapa 3
escolaridades = ["Fundamental", "Medio", "Superior"]
df_nomes = df_nomes.withColumn("Escolaridade", func.lit(escolaridades)[(func.rand() * 3).cast("int")])
df_nomes.show(20)

# Etapa 4
paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Guiana Francesa", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]
df_nomes = df_nomes.withColumn("Pais", func.lit(paises)[(func.rand() * 13).cast("int")])
df_nomes.show(100)

# Etapa 5
df_nomes = df_nomes.withColumn("AnoNascimento", func.lit(1945) + (func.rand() * 66).cast('int'))
df_nomes.show(200)

# Etapa 6
df_select = df_nomes.filter(func.col('AnoNascimento') >= 2000).select('Nome', 'AnoNascimento')
df_select.show(10)

# Etapa 7
df_nomes.createOrReplaceTempView("pessoas")
df_select = spark.sql("SELECT Nome, AnoNascimento FROM pessoas WHERE AnoNascimento >= 2000")
df_select.show(10)

# Etapa 8
millennials = df_nomes.filter((func.col('AnoNascimento') >= 1980) & (func.col('AnoNascimento') <= 1994)).count()
print("Número de pessoas da geração Millennials:", millennials)

# Etapa 9 
df_nomes.createOrReplaceTempView("pessoas")
millennials = spark.sql("SELECT COUNT(AnoNascimento) as TotalMillenials FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")
millennials.show()

# Etapa 10
df_nomes = df_nomes.withColumn('Geracao', func.when((func.col('AnoNascimento') >= 1944) & (func.col('AnoNascimento') <= 1964), 'Baby Boomers')
                                                .when((func.col('AnoNascimento') >= 1965) & (func.col('AnoNascimento') <= 1979), 'Geração X')
                                                .when((func.col('AnoNascimento') >= 1980) & (func.col('AnoNascimento') <= 1994), 'Millennials')
                                                .when((func.col('AnoNascimento') >= 1995) & (func.col('AnoNascimento') <= 2015), 'Geração Z')
                                                .otherwise('Outra'))
df_nomes.createOrReplaceTempView("pessoas")
x_generation = spark.sql("SELECT Pais, Geracao, COUNT(*) AS Quantidade FROM pessoas GROUP BY Pais, Geracao ORDER BY Pais, Geracao")
x_generation.show(52)