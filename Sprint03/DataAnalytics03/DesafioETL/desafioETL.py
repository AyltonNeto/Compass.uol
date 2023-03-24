'''
    <-------ETAPA 01------->
arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

atores = []
qtdd_filmes = []

for dados in linhas[1:]:
    campos = dados.split(',')
    qtdd_filmes.append(campos[2])

for dados in linhas:
    campos = dados.split(',')
    if campos[2] == max(qtdd_filmes):
        print(f'Ator/Atriz:{campos[0]} - Total de Filmes:{campos[2]}')
'''


'''
    <-------ETAPA 02------->
arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

for dados in linhas[1:]:
    if '"Robert Downey, Jr."' in dados:
        dados = dados.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
    campos = dados.split(',')
    print(f'Ator/Atriz:{campos[0]} - Média de Faturamento Bruto:{campos[3]}')
'''


'''
    <-------ETAPA 03------->
arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

atores = []
media_ganho = []

for dados in linhas[1:]:
    campos = dados.split(',')
    atores.append(campos[0])
    media_ganho.append(float(campos[3]))

for dados in linhas[1:]:
    campos = dados.split(',')
    if float(campos[3]) == max(media_ganho):
        print(f"Ator/Atriz:{campos[0]} - Média de Faturamento:{campos[3]}")
'''


'''
    <-------ETAPA 04------->
arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

top_filme = []
mais_frequentes = {}

for dados in linhas[1:]:
    if '"Robert Downey, Jr."' in dados:
        dados = dados.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
    campos = dados.split(',')
    top_filme.append(campos[4])

for filmes in top_filme:
    if top_filme.count(filmes) > 2:
        mais_frequentes[filmes] = top_filme.count(filmes)

lista_ordenada = dict(sorted(mais_frequentes.items(), key=lambda item: item[1], reverse=True))

for item in lista_ordenada:
    print(item,'-', lista_ordenada.get(item),'vezes')
'''

'''
    <-------ETAPA 05------->
arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

atores = []
ganho_total = []

for dados in linhas[1:]:
    if '"Robert Downey, Jr."' in dados:
        dados = dados.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
    campos = dados.split(',')
    ganho_total.append(campos[1])

for item in sorted(ganho_total,reverse=True):
    for dados in linhas[1:]:
        campos = dados.split(',')
        x = [f'{campos[0]} - {campos[1]}']
        if campos[1] == item:
            print(*x)
'''