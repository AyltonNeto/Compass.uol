# Dada as listas a seguir:
#   primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
#   sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
#   idades = [19, 28, 25, 31]

# Faça um programa que imprima o dados na seguinte estrutura: 
#   "índice - primeiroNome sobreNome está com idade anos".

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, nome in enumerate(primeirosNomes):
    i = sobreNomes[indice]
    x = idades[indice]
    print(f'{indice} - {nome} {i} está com {x} anos')


'''
CÓDIGO ALTERNATIVO
(sem usar o comando enumerate)

for i in range(len(idades)):
    print(f'{i} - {primeirosNomes[i]} {sobreNomes[i]} está com {idades[i]} anos') 

'''