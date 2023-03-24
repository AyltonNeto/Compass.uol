def maior_media(x):
    x = media_ganho
    maior_x = max(x)
    index_x = x.index(maior_x)

    nome = atores[index_x]
    print(f"Ator/Atriz:{nome} - Média de Faturamento:{maior_x}")

arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

atores = []
media_ganho = []

for dados in linhas[1:]:
    campos = dados.split(',')
    atores.append(campos[0])
    media_ganho.append(float(campos[3]))
    
maior_media(media_ganho)