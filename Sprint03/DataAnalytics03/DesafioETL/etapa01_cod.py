def maior_qtdd(x):
    x = qtdd_filmes
    maior_x = max(x)
    index_x = x.index(maior_x)

    nome = atores[index_x]
    print(f"Ator/Atriz:{nome} - Total de Filmes:{maior_x}")

arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

atores = []
qtdd_filmes = []

for dados in linhas[1:]:
    campos = dados.split(',')
    atores.append(campos[0])
    qtdd_filmes.append(campos[2])
    
maior_qtdd(qtdd_filmes)