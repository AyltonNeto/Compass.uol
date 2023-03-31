# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
# Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
# Você deverá aplicar as seguintes funções no exercício:
#    map
#    filter
#    sorted
#    sum

# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
#    a lista dos 5 maiores números pares em ordem decrescente;
#    a soma destes valores.

with open('number.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

numeros = []

for dados in linhas:
    corte = dados.split('\n')
    numeros.append(int(corte[0]))

zero_impar = map(lambda x: 0 if x%2 != 0 else x, numeros)
lista = sorted(filter(lambda x: x != 0, zero_impar),reverse=True)

print(lista[:5])
print(sum(lista[:5]))

'''
Utilizei a função map() por obrigação, mas acredito que não faça muito sentido utiliza-la.
Porque não é necessário modificar os elementos contidos na lista, somente filtra-los.


with open('number.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

numeros = []

for dados in linhas:
    corte = dados.split('\n')
    numeros.append(int(corte[0]))

lista = sorted(filter(lambda x: x%2 == 0, numeros),reverse=True)

print(lista[:5])
print(sum(lista[:5]))
'''
