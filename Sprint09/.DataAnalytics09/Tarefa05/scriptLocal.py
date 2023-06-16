from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.types import FloatType, IntegerType
import pyspark.sql.functions as func

spark = SparkSession \
                .builder \
                .master("local[*]")\
                .appName("Exercicio Intro") \
                .getOrCreate()

# 1ª Etapa | Carregar arquivos parquet locais
series_path = "C:/Programação/Projetos/Testes/Sprint09/series.parquet"
tmdb_path = "C:/Programação/Projetos/Testes/Sprint09/tmdb.parquet"

df_dataCSV = spark.read.parquet(series_path)
df_tmdb = spark.read.parquet(tmdb_path)

# 2ª Etapa | Filtrar séries de animação e remover IDs duplicados
df_dataCSV_filter = df_dataCSV.filter( (df_dataCSV['genero'].contains('Animation')) & 
                                    (df_dataCSV['notaMedia'] >= 7.0) & 
                                    (df_dataCSV['numeroVotos'] >= 2500))
df_topSeries = df_dataCSV_filter.dropDuplicates(['id'])

# 3ª Etapa | Unir dataframes dataCSV e tmdb
df_fato = df_topSeries.join(df_tmdb, on='id')
df_fato = df_fato.select('id', 'genero', 'paisOrigem', 'distribuidora', 'estudio', 'emProducao', 'anoLancamento', 'tempoMinutos', 'episodios', 'numeroVotos', 'notaMedia')

# 4ª Etapa | Criação das Dimensões
# Dimensão Serie
df_serie = df_topSeries.select('id', 'tituloPincipal')
df_serie = df_serie.withColumnRenamed('id', 'id_serie')
df_serie = df_serie.withColumnRenamed('tituloPincipal', 'titulo')

# Dimensão Tempo
df_tempo = df_topSeries.withColumn('anoLancamento', df_topSeries['anoLancamento'])
df_tempo = df_tempo.select('anoLancamento').distinct().orderBy('anoLancamento')
df_tempo = df_tempo.withColumn('id_anoLancamento', func.monotonically_increasing_id()+1)
df_tempo = df_tempo.select('id_anoLancamento','anoLancamento')

# Dimensão Pais
df_paisOrigem = df_fato.select('paisOrigem').distinct().orderBy('paisOrigem')
df_paisOrigem = df_paisOrigem.withColumn('id_pais', func.monotonically_increasing_id() + 1)
df_paisOrigem = df_paisOrigem.select('id_pais','paisOrigem')

# Dimensão Status
df_status = df_fato.select('emProducao').distinct()
df_status = df_status.withColumn('status', func.when(df_fato['emProducao'] == 'true', 'Em Produção').otherwise('Finalizado'))
df_status = df_status.withColumn('id_status', func.monotonically_increasing_id()+1)
df_status = df_status.select('id_status','status')

# Dimensão Estúdio
df_estudio = df_fato.select('estudio').distinct().orderBy('estudio').filter(df_fato['estudio'].isNotNull())
df_estudio = df_estudio.withColumn('id_estudio', func.monotonically_increasing_id()+1)
df_estudio = df_estudio.select('id_estudio','estudio')

# Dimensão Distribuidora
df_distribuidora = df_fato.select('distribuidora').distinct().orderBy('distribuidora').filter(df_fato['distribuidora'].isNotNull())
df_distribuidora = df_distribuidora.withColumn('id_distribuidora', func.monotonically_increasing_id()+1)
df_distribuidora = df_distribuidora.select('id_distribuidora','distribuidora')

# 5ª Etapa | Criando Dimensão Fato através de joins
# Join com a dimensão Tempo
df_fato = df_fato.join(df_tempo, on='anoLancamento', how='left')
df_fato = df_fato.drop('anoLancamento')

# Join com a dimensão de País
df_fato = df_fato.join(df_paisOrigem, on='paisOrigem', how='left')
df_fato = df_fato.drop('paisOrigem')

# Join com a dimensão de Status
df_fato = df_fato.withColumn('emProducao', func.when(df_fato['emProducao'] == 'true', 'Em Produção').otherwise('Finalizado'))
df_fato = df_fato.join(df_status, df_fato['emProducao'] == df_status['status'], how='left')
df_fato = df_fato.drop('emProducao', 'status')

# Join com a dimensão de Estúdio
df_fato = df_fato.join(df_estudio, on='estudio', how='left')
df_fato = df_fato.drop('estudio')

# Join com a dimensão de Distribuidora
df_fato = df_fato.join(df_distribuidora, on='distribuidora', how='left')
df_fato = df_fato.drop('distribuidora')

# Selecionando e renomeando colunas da tabela Fato
df_fato = df_fato.withColumnRenamed('id', 'id_serie')
df_fato = df_fato.select('id_serie', 'id_pais', 'id_distribuidora', 'id_estudio', 'id_status', 'id_anoLancamento', 'tempoMinutos', 'episodios', 'numeroVotos', 'notaMedia', 'genero').orderBy(func.desc('numeroVotos'))


df_serie.show()
df_tempo.show()
df_paisOrigem.show()
df_status.show()
df_distribuidora.show()
df_estudio.show()
df_fato.show()