# Relatório da Sprint 08
Nessa Sptint aprendi a utilizar a API do TMDB e a fazer extrações de dados para enriquicer o arquivo CSV disponibilizado, visando a realização de um projeto de análise posterior. Também pude praticar como gerar dados aleatórios em Python e a utilizar o PySpark para a criação de DataFrames e Tabelas, leitura de arquivos CSV e a utilização do comandos SQL no Spark.

## Criando conta no TMDB e Testando a API
![ContaTMDB](https://github.com/AyltonNeto/Compass.uol/blob/b17ad7afd3dc679c7b37e88f2b721f133bff9a84/Sprint08/.DataAnalytics08/Tarefa01/1.ContaTMDB.png)

![TesteAPI](https://github.com/AyltonNeto/Compass.uol/blob/b17ad7afd3dc679c7b37e88f2b721f133bff9a84/Sprint08/.DataAnalytics08/Tarefa01/2.TestandoAPI.png)

## Definição de tema e extração de dados do TMDB para enriquecer o projeto.
### Tema: Análise do Cenário de Boas Séries de Animações
#### Escolha do Tema
Para a escolha do tema, me coloquei no lugar de um cliente que gostaria de lançar uma série de animação que precisa de uma boa análise do cenário de animações mundial. O cliente precisa de dados relevantes, sobre os gêneros que mais fazem sucesso, bem como a origem, a duração e as principais distribuidora.

### Filtrar Boas Animações
Antes de extrair os dados, pensei em como escolheria as séries consideradas "boas". Então realizei algumas filtragens no arquivo series.csv localmente e decidi extrair as animações com nota maior ou igual a 7.0 e com pelo menos 2.500 avaliações. Esses critérios abrangem muitas animações permitindo fazer muitas análises, porém, posteriormente será necessário fazer uma seleção mais criteriosa para que a análise se baseie nas melhores séries.

![SelecaoBoasAnimacoes](https://github.com/AyltonNeto/Compass.uol/assets/83987476/c5f47368-e1e9-454f-9a53-a7f8ec1f4a47)

### Extrair Dados do TMDB 
Devido aos IDs disponibilzados no arquivo CSV muitas das vezes não coincindirem com os do TMDB, pesquisei bastnte e descobri que esses IDs vinham do IMDB. Então precisei elaborar uma função que não somente extraisse os dados do TMDB, mas antes, encontrasse o ID correto para fazer a busca das animações.

![FuncaoExtracao](https://github.com/AyltonNeto/Compass.uol/assets/83987476/4c14c16a-fc31-4942-9b5d-243ce811f420)

### Explicação do Código Lambda
Depois de definir tudo o que seria feito localmente, refiz o código para que funcionasse no Lambda. O meu código pode ser dividido em 5 partes: 

O primeiro trecho contem as bibliotecas e as chaves utilizadas;

![Trecho1](https://github.com/AyltonNeto/Compass.uol/assets/83987476/92d07006-bc2b-4fbd-a726-cd3f95303b5c)

O segundo a função que obtem o id correto e em seguida faz a busca no TMDB; 

![Trecho2](https://github.com/AyltonNeto/Compass.uol/assets/83987476/c1d18cd2-6778-4fc5-bc63-568168238d67)

O terceiro, localiza e filtra o arquivo CSV no bucket, selecionando as "boas" animações e armazena em uma variável; 

![Trecho3](https://github.com/AyltonNeto/Compass.uol/assets/83987476/223c5d4f-1d56-40dc-81ef-dac74e242f77)

O quarto trecho consiste em um looping que utiliza a função criada anteriormente para preencher cada campo com os dados que foram extraidos e colocá-los um a um em uma lista (caso retorne algum valor); 

![Trecho4](https://github.com/AyltonNeto/Compass.uol/assets/83987476/67fd1fe7-a252-4824-9aea-9f964c6cec22)

O quinto trecho está dentro do looping e cria um arquivo JSON dentro do bucket a cada 100 resultados ou quando chegar ao fim da seleção.

![Trecho5](https://github.com/AyltonNeto/Compass.uol/assets/83987476/c770ed2a-574b-4a9a-8939-6cf179b7478d)

## Exercícios de Geração de Massa de Dados

## Exercicios Spark

### Imports:

    from pyspark.sql import SparkSession
    from pyspark import SparkContext, SQLContext
    import pyspark.sql.functions as func

### Etapa 1: 
##### Ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv. Carrega-lo para dentro de um dataframe chamado df_nomes e listar algumas linhas através do método show.

    df_nomes = spark.read.csv("C:/Programação/Projetos/Compass.uol/Sprint08/.DataAnalytics08/Tarefa03/nomes_aleatorios.txt")
    df_nomes.show(5)

        +----------------+
        |             _c0|
        +----------------+
        |  Frances Bennet|
        |   Jamie Russell|
        |  Edward Kistler|
        |   Sheila Maurer|
        |Donald Golightly|
        +----------------+

### Etapa 2
##### Renomear a coluna para Nomes, imprimir o esquema e mostrar 10 linhas do dataframe.
    
    df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")
    df_nomes.printSchema()
        |-- Nome: string (nullable = true)
    df_nomes.show(10)
        +-----------------+
        |             Nome|
        +-----------------+
        |   Frances Bennet|
        |    Jamie Russell|
        |   Edward Kistler|
        |    Sheila Maurer|
        | Donald Golightly|
        |       David Gray|
        |      Joy Bennett|
        |      Paul Kriese|
        |Berniece Ornellas|
        |    Brian Farrell|
        +-----------------+

### Etapa 3
##### Adicione uma nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória: Fundamental, Medio ou Superior.

    escolaridades = ["Fundamental", "Medio", "Superior"]
    df_nomes = df_nomes.withColumn("Escolaridade", func.lit(escolaridades)[(func.rand() * 3).cast("int")])
    df_nomes.show(20)
        +-----------------+------------+
        |   Frances Bennet|    Superior|
        |    Jamie Russell| Fundamental|
        |   Edward Kistler|       Medio|
        |    Sheila Maurer|    Superior|
        | Donald Golightly| Fundamental|
        |       David Gray| Fundamental|
        |      Joy Bennett|    Superior|
        |      Paul Kriese| Fundamental|
        |Berniece Ornellas|    Superior|
        |    Brian Farrell| Fundamental|
        +-----------------+------------+

### Etapa 4
##### Adicione uma nova coluna chamada Pais e atribua para cada linha o nome de um dos 13 países da América do Sul, de forma aleatória.
    
    paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Guiana Francesa", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]
    df_nomes = df_nomes.withColumn("Pais", func.lit(paises)[(func.rand() * 13).cast("int")])
    df_nomes.show(20)

        +-----------------+------------+---------------+
        |             Nome|Escolaridade|           Pais|
        +-----------------+------------+---------------+
        |   Frances Bennet|    Superior|        Bolivia|
        |    Jamie Russell| Fundamental|        Equador|
        |   Edward Kistler|       Medio|          Chile|
        |    Sheila Maurer|    Superior|         Brasil|
        | Donald Golightly| Fundamental|         Brasil|
        |       David Gray| Fundamental|        Bolivia|
        |      Joy Bennett|    Superior|Guiana Francesa|
        |      Paul Kriese| Fundamental|         Brasil|
        |Berniece Ornellas|    Superior|        Bolivia|
        |    Brian Farrell| Fundamental|        Equador|
        |   Kara Mcelwaine|       Medio|        Bolivia|
        |    Tracy Herring| Fundamental|        Bolivia|
        |  Howard Lazarine|    Superior|         Guiana|
        |     Leroy Strahl|    Superior|         Brasil|
        |     Ernest Hulet| Fundamental|         Guiana|
        |     David Medina| Fundamental|        Uruguai|
        |   Lorenzo Woodis| Fundamental|Guiana Francesa|
        |      Page Marthe|    Superior|        Bolivia|
        |   Herbert Morris|       Medio|        Equador|
        |      Albert Leef| Fundamental|         Guiana|
        +-----------------+------------+---------------+

### Etapa 5
##### Adicione uma nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010, de forma aleatória. 
   
    df_nomes = df_nomes.withColumn("AnoNascimento", func.lit(1945) + (func.rand() * 66).cast('int'))
    df_nomes.show(20)
        +-----------------+------------+---------------+-------------+
        |             Nome|Escolaridade|           Pais|AnoNascimento|
        +-----------------+------------+---------------+-------------+
        |   Frances Bennet|    Superior|        Bolivia|         2008|
        |    Jamie Russell| Fundamental|        Equador|         1976|
        |   Edward Kistler|       Medio|          Chile|         1981|
        |    Sheila Maurer|    Superior|         Brasil|         1976|
        | Donald Golightly| Fundamental|         Brasil|         1998|
        |       David Gray| Fundamental|        Bolivia|         1994|
        |      Joy Bennett|    Superior|Guiana Francesa|         1945|
        |      Paul Kriese| Fundamental|         Brasil|         1972|
        |Berniece Ornellas|    Superior|        Bolivia|         2008|
        |    Brian Farrell| Fundamental|        Equador|         1966|
        |   Kara Mcelwaine|       Medio|        Bolivia|         2002|
        |    Tracy Herring| Fundamental|        Bolivia|         1947|
        |  Howard Lazarine|    Superior|         Guiana|         1992|
        |     Leroy Strahl|    Superior|         Brasil|         1994|
        |     Ernest Hulet| Fundamental|         Guiana|         1981|
        |     David Medina| Fundamental|        Uruguai|         1994|
        |   Lorenzo Woodis| Fundamental|Guiana Francesa|         1979|
        |      Page Marthe|    Superior|        Bolivia|         1957|
        |   Herbert Morris|       Medio|        Equador|         1953|
        |      Albert Leef| Fundamental|         Guiana|         1949|
        +-----------------+------------+---------------+-------------+


### Etapa 6
##### Usando o método select, selecione as pessoas que nasceram neste século. Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste.

    df_select = df_nomes.filter(func.col('AnoNascimento') >= 2000).select('Nome')
    df_select.show(10)
        +-----------------+
        |   Frances Bennet|
        |Berniece Ornellas|
        |   Kara Mcelwaine|
        |         Mary Lee|
        |   Wilfredo Grant|
        |    Lynne Dustman|
        |      Milton Rowe|
        |     Ida Randazzo|
        |    Joann Ballard|
        |George Fiorentino|
        +-----------------+

### Etapa 7
##### Usando Spark SQL repita o processo da Pergunta 6

    df_nomes.createOrReplaceTempView("pessoas")
    df_select = spark.sql("SELECT Nome FROM pessoas WHERE AnoNascimento >= 2000")
    df_select.show(10)
        +-----------------+
        |   Frances Bennet|
        |Berniece Ornellas|
        |   Kara Mcelwaine|
        |         Mary Lee|
        |   Wilfredo Grant|
        |    Lynne Dustman|
        |      Milton Rowe|
        |     Ida Randazzo|
        |    Joann Ballard|
        |George Fiorentino|
        +-----------------+

### Etapa 8
##### Usando o método select, Conte o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) no Dataset
    
    millennials = df_nomes.filter((func.col('AnoNascimento') >= 1980) & (func.col('AnoNascimento') <= 1994)).count()
    print("Número de pessoas da geração Millennials:", millennials)
        Número de pessoas da geração Millennials: 2273219

### Etapa 9 
##### Repita o processo da Pergunta 8 utilizando Spark SQL
    
    df_nomes.createOrReplaceTempView("pessoas")
    millennials = spark.sql("SELECT COUNT(AnoNascimento) as TotalMillenials FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")
    millennials.show()

        +---------------+
        |TotalMillenials|
        +---------------+
        |        2273219|
        +---------------+


### Etapa 10
##### Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações abaixo. Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade
    
    df_nomes = df_nomes.withColumn('Geracao', 
        func.when((func.col('AnoNascimento') >= 1944) & (func.col('AnoNascimento') <= 1964), 'Baby Boomers')
            .when((func.col('AnoNascimento') >= 1965) & (func.col('AnoNascimento') <= 1979), 'Geração X')
            .when((func.col('AnoNascimento') >= 1980) & (func.col('AnoNascimento') <= 1994), 'Millennials')
            .when((func.col('AnoNascimento') >= 1995) & (func.col('AnoNascimento') <= 2015), 'Geração Z')
            .otherwise('Outra'))

    df_nomes.createOrReplaceTempView("pessoas")

    generations = spark.sql("SELECT Pais, Geracao, COUNT(*) AS Quantidade FROM pessoas GROUP BY Pais, Geracao ORDER BY Pais, Geracao")

    generations.show(52)

        +---------------+------------+----------+
        |           Pais|     Geracao|Quantidade|
        +---------------+------------+----------+
        |      Argentina|Baby Boomers|    233213|
        |      Argentina|   Geração X|    174382|
        |      Argentina|   Geração Z|    186375|
        |      Argentina| Millennials|    174275|
        |        Bolivia|Baby Boomers|    232214|
        |        Bolivia|   Geração X|    174803|
        |        Bolivia|   Geração Z|    186397|
        |        Bolivia| Millennials|    174896|
        |         Brasil|Baby Boomers|    233357|
        |         Brasil|   Geração X|    175252|
        |         Brasil|   Geração Z|    186007|
        |         Brasil| Millennials|    174922|
        |          Chile|Baby Boomers|    233052|
        |          Chile|   Geração X|    175576|
        |          Chile|   Geração Z|    185961|
        |          Chile| Millennials|    175121|
        |       Colombia|Baby Boomers|    232634|
        |       Colombia|   Geração X|    174668|
        |       Colombia|   Geração Z|    186049|
        |       Colombia| Millennials|    175148|
        |        Equador|Baby Boomers|    234105|
        |        Equador|   Geração X|    174712|
        |        Equador|   Geração Z|    186654|
        |        Equador| Millennials|    174677|
        |         Guiana|Baby Boomers|    233741|
        |         Guiana|   Geração X|    174871|
        |         Guiana|   Geração Z|    186153|
        |         Guiana| Millennials|    175556|
        |Guiana Francesa|Baby Boomers|    232794|
        |Guiana Francesa|   Geração X|    174896|
        |Guiana Francesa|   Geração Z|    186187|
        |Guiana Francesa| Millennials|    174458|
        |       Paraguai|Baby Boomers|    232898|
        |       Paraguai|   Geração X|    174392|
        |       Paraguai|   Geração Z|    186282|
        |       Paraguai| Millennials|    175253|
        |           Peru|Baby Boomers|    233539|
        |           Peru|   Geração X|    175276|
        |           Peru|   Geração Z|    186047|
        |           Peru| Millennials|    174904|
        |       Suriname|Baby Boomers|    232965|
        |       Suriname|   Geração X|    175488|
        |       Suriname|   Geração Z|    186432|
        |       Suriname| Millennials|    174378|
        |        Uruguai|Baby Boomers|    233593|
        |        Uruguai|   Geração X|    175320|
        |        Uruguai|   Geração Z|    186155|
        |        Uruguai| Millennials|    175170|
        |      Venezuela|Baby Boomers|    232923|
        |      Venezuela|   Geração X|    174793|
        |      Venezuela|   Geração Z|    186625|
        |      Venezuela| Millennials|    174461|
        +---------------+------------+----------+
