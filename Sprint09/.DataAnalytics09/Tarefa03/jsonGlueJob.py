import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

json_paths = [
    "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas0.json",
    "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas1.json",
    "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas2.json",
    "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas3.json",
    "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas4.json",
    "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas5.json"
]

json_data = spark.read.json(json_paths)
json_data = json_data.repartition(1)
json_data.write.mode("append").parquet("s3://data-lake-do-aylton/Trusted/TMDB/")

job.commit()