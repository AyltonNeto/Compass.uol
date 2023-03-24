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
    mais_frequentes[filmes] = top_filme.count(filmes)

for filme, freq in mais_frequentes.items():
    if freq == max(mais_frequentes.values()):
        nome = filme
        break

print(f'O Filme Mais Frequente: {nome} - Frequencia: {max(mais_frequentes.values())} vezes')

lista_ordenada = dict(sorted(mais_frequentes.items(), key=lambda item: item[1], reverse=True))
top5 = list(lista_ordenada)

print('')
print('--Rank dos 5 Filmes Mais Frequentes--')
for item in top5[:5]:
    print(f'Filme: {item} - Frequencia: {lista_ordenada.get(item)} vezes')