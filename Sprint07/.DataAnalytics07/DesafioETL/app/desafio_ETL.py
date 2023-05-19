import boto3

user = boto3.client(
    service_name='s3',
    aws_access_key_id='AKIAXEBR7233ZTFJKCQS',
    aws_secret_access_key='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',
    region_name='us-east-1'
)

pasta_movies = f'Raw/Local/CSV/Movies/2023/05/17/movies.csv'
pasta_series = f'Raw/Local/CSV/Series/2023/05/17/series.csv'

user.upload_file('movies.csv', 'data-lake-aylton', pasta_movies)
user.upload_file('series.csv', 'data-lake-aylton', pasta_series)