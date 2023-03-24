arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

atores = []
ganho_total = []

for dados in linhas[1:]:
    if '"Robert Downey, Jr."' in dados:
        dados = dados.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
    campos = dados.split(',')
    x = [f'{campos[0]} - {campos[1]}']
    print(*x)