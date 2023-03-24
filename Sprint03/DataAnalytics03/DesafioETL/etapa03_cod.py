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