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