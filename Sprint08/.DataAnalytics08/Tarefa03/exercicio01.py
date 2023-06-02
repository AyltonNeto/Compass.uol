import random

numeros = random.sample(range(0,10000),250)
ordenar_numeros = sorted(numeros, reverse=True)
print(ordenar_numeros)