import json
import requests
import pandas as pd
import boto3

def lambda_handler(event, context):
    
    user = boto3.client(
    service_name='s3',
    aws_access_key_id='my_AWS_key',
    aws_secret_access_key='my_secret_AWS_key',
    region_name='us-east-1'
    )
    
    api_key = 'my_api_key'
    
    # Função para obter o TMDB(ID) pelo IMDB(ID) e extrair dados da API, caso encontre algum resultado.
    def get_data_TMDB(id_IMDB, api_key):
        url = f'https://api.themoviedb.org/3/find/{id_IMDB}?api_key={api_key}&external_source=imdb_id'
        response1 = requests.get(url)
        data1 = response1.json()
    
        if 'tv_results' in data1 and len(data1['tv_results']) > 0:
            id_TMDB = data1['tv_results'][0]['id']
            url = f'https://api.themoviedb.org/3/tv/{id_TMDB}?api_key={api_key}'
            response2 = requests.get(url)
            data2 = response2.json()
            return data2
        return None
    
    response = user.get_object(Bucket='data-lake-do-aylton', Key='Raw/Local/CSV/Series/2023/05/29/series.csv')
    data_CSV = pd.read_csv(response['Body'], sep='|')
    
    filter_animations = data_CSV.loc[(data_CSV['genero'].str.contains('Animation')) & 
                                (data_CSV['notaMedia'] >= 7.0) & 
                                (data_CSV['numeroVotos'] >= 2500)]
    
    top_series = filter_animations[[
        'id',
        'tituloPincipal', 
        'anoLancamento', 
        'notaMedia',
        'numeroVotos',
        'genero']]
    
    df = top_series.drop_duplicates(subset='id').sort_values(by='numeroVotos', ascending=False)

    series_informations = []
    count, num_json = 0, 0

    for index, row in enumerate(df.iterrows()):
        id_IMDB = str(row[1]['id'])
        series_details = get_data_TMDB(id_IMDB, api_key)
        
        if series_details != None:
            title = series_details['name']
            origin = series_details['origin_country']
            company = series_details['production_companies'][0]['name'] if series_details['production_companies'] else None
            network = series_details['networks'][0]['name'] if series_details['networks'] else None
            production = series_details['in_production']
            episodes = series_details['number_of_episodes']
            seasons = series_details['number_of_seasons']
            time = series_details['episode_run_time']

            dic_details = {
                'id': id_IMDB,
                'titulo': title,
                'estudio': company,
                'distribuidora': network,
                'duracao': time,
                'episodios': episodes,
                'temporadas': seasons,
                'emProducao': production
            }
            
            series_informations.append(dic_details)
            count += 1
            
            if count % 100 == 0 or index == len(df)-1:
                json_informations = json.dumps(series_informations)
                user.put_object(Body=json_informations, Bucket='data-lake-do-aylton', Key=f'Raw/TMDB/JSON/2023/05/29/series_datas{num_json}.json')
                series_informations = []
                num_json += 1
            continue

    return {
        "statusCode": 200,
        "body": "Arquivo JSON criado com sucesso."
    }

