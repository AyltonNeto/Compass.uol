# Relatório da Sprint 09
Nessa Sprint começamos aprendendo sobre Modelagem Relacional e Modelagem Dimensional, apesar de já conhecer a relacional, tivemos que nos aprofundar bastante para compreender os modelos, os componentes e principalmente sobre a normalização, já a dimensional foi novidade pra mim, aprendemos seus modelos, elementos e  sobre sua importancia para a construção de Data Warehouses. Após compreender a parte teórica partimos para prática e fizemos nossa prórpia normalização e construção de uma tabela dimensional. Em relação ao projeto, fizemos o processamento dos dados na Trusted, criamos um modelo dimensional utilizando nossos dados e refinamos os dados que serão utilizados na Refined, para realizar as etapas do projeto utilizamos principalmente o Glue.

## Tarefa 1 - Modelagem Relacional
### Normalização
Nesta tarefa o objetivo foi pegar um banco de dados e fazer a sua normalização utilizando comandos em um SQL Cliente. o código criado foi divido em 3 partes: a primeira renomeia 'tb_locacao' para 'tb_locacaoOriginal' para evitar modificar os dados base; depois são criadas todas as tabelas com seus respectivos valores e chaves; por fim as tabelas são preenchidas com base na 'tb_locacaoOriginal'.

![TabelasCriadas](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa01/TabelasCriadas.png)

##### Modelo Normalizado
![TabelasNormalizadas](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa01/TabelasNormalizadas.png)

## Tarefa 2 - Modelagem Dimensional
### Criação de Modelo
Já nesta tarefa, utilizei as tabelas criadas anteriomente para gerar visualizações de acordo com o modelo dimensional.

![ViewsCriadas](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa02/ViewsCriadas.png)

##### Modelo Dimensional
![ViewsModeloDimensional](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa02/ViewsModeloDimensional.png)

## Tarefa 3 - Desafio Parte 3 
### Processamento da Trusted
Essa tarefa inicia a parte 3 do desafio final. O objetivo foi fazer 2 jobs no Glue para transformar os arquivos (series.csv e os json extraídos do TMDB) que serão utilizados nas análise. Para isso, criei um código que extrai o conteúdo dos arquivos no bucket, transforma esses arquivos em parquet e os coloca em uma pasta chamada Trusted.

![JobsGlue](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa03/Jobs.png)

#### Códigos utilizados sem a parte inicial padrão do Glue para scripts spark

##### Código 1:
  
    csv_path = "s3://data-lake-do-aylton/Raw/Local/CSV/Series/2023/05/29/series.csv"
    
    csv_data = spark.read.format("csv").option("header", "true").option("delimiter", "|").load(csv_path)
    csv_data = csv_data.repartition(1)
    csv_data.write.mode("append").parquet("s3://data-lake-do-aylton/Trusted/CSV/")
    
    job.commit()

##### Código 2:
  
    json_paths = [
        "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas0.json",
        "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas1.json",
        "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas2.json",
        "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas3.json",
        "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas4.json",
        "s3://data-lake-do-aylton/Raw/TMDB/JSON/2023/05/31/series_datas5.json"
    ']
  
    json_data = spark.read.json(json_paths)
    json_data = json_data.repartition(1)
    json_data.write.mode("append").parquet("s3://data-lake-do-aylton/Trusted/TMDB/")
    
    job.commit()
    
##### Resultado no Bucket
![Trusted](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa03/Trusted.png)

## Tarefa 4 - Desafio Parte 3
### Modelagem de Dados da Refined
Nesta tarefa, elaborei um modelo dimensional para os dados que serão utilizados no Projeto Final.

![ModelagemDimensional](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa04/Modelagem_Dimensional.png)

## Tarefa 5 - Desafio Parte 3
### Processamento da Refined
Na útima tarefa, o objetivo foi aplicar o modelo dimensional elaborado na tarefa 4. 
Para isso, tive que criar um database e fazer mais um script no Glue.

##### Database Criado
![CriandoDataBase](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa04/CriandoDatabase.png)

##### Script para gerar as dimensões e a tabela fato na pasta Refined, código abaixo:

###### 1ª Etapa | Carregar arquivos parquet do Bucket
    
    series_path = 's3://data-lake-do-aylton/Trusted/CSV/series.parquet'
    tmdb_path = 's3://data-lake-do-aylton/Trusted/TMDB/tmdb.parquet'
    
    df_dataCSV = spark.read.parquet(series_path)
    df_tmdb = spark.read.parquet(tmdb_path)
    
###### 2ª Etapa | Filtrar séries de animação e remover IDs duplicados

    df_dataCSV_filter = df_dataCSV.filter( (df_dataCSV['genero'].contains('Animation')) & 
                                        (df_dataCSV['notaMedia'] >= 7.0) & 
                                        (df_dataCSV['numeroVotos'] >= 2500))
    df_topSeries = df_dataCSV_filter.dropDuplicates(['id'])
    
###### 3ª Etapa | Unir dataframes dataCSV e tmdb
 
    df_fato = df_topSeries.join(df_tmdb, on='id')
    
###### 4ª Etapa | Criação das Dimensões
    
    # Dimensão Serie
    df_serie = df_fato.select('id', 'tituloPincipal')
    df_serie = df_serie.withColumnRenamed('id', 'id_serie')
    df_serie = df_serie.withColumnRenamed('tituloPincipal', 'titulo')
    
    # Dimensão Tempo
    df_tempo = df_fato.withColumn('anoLancamento', df_fato['anoLancamento'])
    df_tempo = df_tempo.select('anoLancamento').distinct().orderBy('anoLancamento')
    df_tempo = df_tempo.withColumn('id_anoLancamento', func.monotonically_increasing_id()+1)
    df_tempo = df_tempo.select('id_anoLancamento','anoLancamento')
    
    # Dimensão PaísOrigem
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
    
###### 5ª Etapa | Criação da Tabela Fato através de joins
    
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
    
###### 6ª Etapa | Salvar os dataframes como tabelas em formato Parquet na Refined
    
    df_serie.repartition(1).write.saveAsTable(name='project_animations.dim_serie',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Serie',format='parquet')
    df_tempo.repartition(1).write.saveAsTable(name='project_animations.dim_tempo',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Tempo',format='parquet')
    df_paisOrigem.repartition(1).write.saveAsTable(name='project_animations.dim_paisOrigem',mode='overwrite',path='s3://data-lake-do-aylton/Refined/PaisOrigem',format='parquet')
    df_status.repartition(1).write.saveAsTable(name='project_animations.dim_status',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Status',format='parquet')
    df_distribuidora.repartition(1).write.saveAsTable(name='project_animations.dim_distribuidora',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Distribuidora',format='parquet')
    df_estudio.repartition(1).write.saveAsTable(name='project_animations.dim_estudio',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Estudio',format='parquet')
    df_fato.repartition(1).write.saveAsTable(name='project_animations.fato_series',mode='overwrite',path='s3://data-lake-do-aylton/Refined/Fato',format='parquet')
    
    job.commit()

##### Resultado no Bucket
![Refined](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa05/Refined.png)

##### Database Preenchido com as Dimensões
![TabelasCriadas](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa05/TabelasCriadas.png)

##### Resultado no Athena
![Athena](https://github.com/AyltonNeto/Compass.uol/blob/bdba84759669fa0dd0fa5b79d37ddf9d7589674b/Sprint09/.DataAnalytics09/Tarefa05/TabelasAthena.png)
