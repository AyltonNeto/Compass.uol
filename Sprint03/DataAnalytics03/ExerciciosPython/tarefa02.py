# Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. 
# Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).

# Importante: Aplique a função range() em seu código.

for i in range(3):
    num = int(input())
    if num % 2 == 0:
        print('Par:',num)
    else: print('Ímpar:',num) 