arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

for dados in linhas[1:]:
    if '"Robert Downey, Jr."' in dados:
        dados = dados.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
    campos = dados.split(',')
    print(f'Ator/Atriz:{campos[0]} - Média de Faturamento Bruto:{campos[3]}')
