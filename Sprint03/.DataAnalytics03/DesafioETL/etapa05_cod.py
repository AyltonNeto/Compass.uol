arquivo = open('actors.csv', 'r')
linhas = arquivo.readlines()

atores = []
ganho_total = []

for dados in linhas[1:]:
    if '"Robert Downey, Jr."' in dados:
        dados = dados.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
    campos = dados.split(',')
    x = [f'Ator/Atriz:{campos[0]} - Faturamento Bruto Total:{campos[1]}']
    print(*x)

# -----------------------------ATENÇÃO--------------------------------
# Observações: A coluna "Total Gross" já estava em ordem Decrescente,
# então não achei necessário utilizar um códico para colocar em ordem.
# Mas caso fosse necessário ordenar, deixo o código completo abaixo:

'''
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