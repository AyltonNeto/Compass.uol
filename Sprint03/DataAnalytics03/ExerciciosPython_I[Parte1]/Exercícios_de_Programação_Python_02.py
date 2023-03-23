# Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. 
# Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).

# Importante: Aplique a função range() em seu código.

def isPar(num):
    if num%2 == 0:
        print('Par:',num)
    else: print('Ímpar:',num) 

num1 = int(input())
num2 = int(input())
num3 = int(input())

isPar(num1)
isPar(num2)
isPar(num3)

