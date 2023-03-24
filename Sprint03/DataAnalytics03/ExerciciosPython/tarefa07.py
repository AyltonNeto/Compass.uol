# Dada a seguinte lista:
#   a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Faça um programa que gere uma nova lista contendo apenas números ímpares.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista = []

for i in a:
    if i % 2 != 0:
        lista.append(i)
print(lista)


'''
CÓDIGO ALTERNATIVO

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(a[::2])

'''