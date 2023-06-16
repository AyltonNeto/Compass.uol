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

csv_path = "s3://data-lake-do-aylton/Raw/Local/CSV/Series/2023/05/29/series.csv"

csv_data = spark.read.format("csv").option("header", "true").option("delimiter", "|").load(csv_path)
csv_data = csv_data.repartition(1)
csv_data.write.mode("append").parquet("s3://data-lake-do-aylton/Trusted/CSV/")

job.commit()