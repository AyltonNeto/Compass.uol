# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada! 
#   import random 
#   amostra aleatoriamente 50 números do intervalo 0...500
#   random_list = random.sample(range(500),50)

# Use as variáveis abaixo para representar cada operação matemática
#   mediana
#   media
#   valor_minimo 
#   valor_maximo 


import random 
random_list = random.sample(range(500),50)
print(random_list)

lista_ordem = sorted(random_list)
soma = 0

for i in random_list:
    soma += i

mediana = (lista_ordem[24]+lista_ordem[25])/2
media = (soma/50)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(mediana, media, valor_minimo, valor_maximo)


# CÓDIGO ALTERNATIVO
import statistics
import random 
random_list = random.sample(range(500),50)
print(random_list)

mediana = statistics.median(random_list)
media = statistics.mean(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(mediana, media, valor_minimo, valor_maximo)
