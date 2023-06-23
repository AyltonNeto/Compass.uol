import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.window import Window
import pyspark.sql.functions as func



## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Carregar arquivos parquet do Bucket
series_path = 's3://data-lake-do-aylton/Trusted/CSV/series.parquet'
tmdb_path = 's3://data-lake-do-aylton/Trusted/TMDB/tmdb.parquet'

df_dataCSV = spark.read.parquet(series_path)
df_tmdb = spark.read.parquet(tmdb_path)

# 2ª Etapa | Filtrar séries de animação e remover IDs duplicados
df_dataCSV_filter = df_dataCSV.filter( (df_dataCSV['genero'].contains('Animation')) & 
                                    (df_dataCSV['notaMedia'] >= 7.0) & 
                                    (df_dataCSV['numeroVotos'] >= 2500))
df_topSeries = df_dataCSV_filter.dropDuplicates(['id'])

# 3ª Etapa | Unir dataframes dataCSV e tmdb
df_fato = df_topSeries.join(df_tmdb, on='id')

# 4ª Etapa | Criação das Dimensões
# Dimensão Serie
df_serie = df_fato.select('id', 'tituloPincipal')
df_serie = df_serie.withColumnRenamed('id', 'id_serie')
df_serie = df_serie.withColumnRenamed('tituloPincipal', 'titulo')

# Dimensão Tempo
df_tempo = df_fato.select('anoLancamento').distinct().orderBy('anoLancamento')
df_tempo = df_tempo.withColumn('id_anoLancamento', func.row_number().over(Window.orderBy('anoLancamento')))
df_tempo = df_tempo.select('id_anoLancamento','anoLancamento')

# Dimensão PaísOrigem
df_paisOrigem = df_fato.select('paisOrigem').distinct().orderBy('paisOrigem')
df_paisOrigem = df_paisOrigem.withColumn('id_pais', func.row_number().over(Window.orderBy('paisOrigem')))
df_paisOrigem = df_paisOrigem.select('id_pais','paisOrigem')

# Dimensão Status
df_status = df_fato.select('emProducao').distinct()
df_status = df_status.withColumn('status', func.when(df_fato['emProducao'] == 'true', 'Em Produção').otherwise('Finalizado'))
df_status = df_status.withColumn('id_status', func.row_number().over(Window.orderBy('status')))
df_status = df_status.select('id_status','status')

# Dimensão Estúdio
df_estudio = df_fato.select('estudio').distinct().orderBy('estudio').filter(df_fato['estudio'].isNotNull())
df_estudio = df_estudio.withColumn('id_estudio', func.row_number().over(Window.orderBy('estudio')))
df_estudio = df_estudio.select('id_estudio','estudio')

# Dimensão Distribuidora
df_distribuidora = df_fato.select('distribuidora').distinct().orderBy('distribuidora').filter(df_fato['distribuidora'].isNotNull())
df_distribuidora = df_distribuidora.withColumn('id_distribuidora', func.row_number().over(Window.orderBy('distribuidora')))
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

# 6 Etapa | Salvar os dataframes como tabelas em formato Parquet na Refined
df_serie.repartition(1).write.saveAsTable(name='project_animations.dim_serie',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Serie',format='parquet')
df_tempo.repartition(1).write.saveAsTable(name='project_animations.dim_tempo',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Tempo',format='parquet')
df_paisOrigem.repartition(1).write.saveAsTable(name='project_animations.dim_paisOrigem',mode='overwrite',path='s3://data-lake-do-aylton/Refined/PaisOrigem',format='parquet')
df_status.repartition(1).write.saveAsTable(name='project_animations.dim_status',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Status',format='parquet')
df_distribuidora.repartition(1).write.saveAsTable(name='project_animations.dim_distribuidora',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Distribuidora',format='parquet')
df_estudio.repartition(1).write.saveAsTable(name='project_animations.dim_estudio',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Estudio',format='parquet')
df_fato.repartition(1).write.saveAsTable(name='project_animations.fato_series',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Fato',format='parquet')

job.commit()