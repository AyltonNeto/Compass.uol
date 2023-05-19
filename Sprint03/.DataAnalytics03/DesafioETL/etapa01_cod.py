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