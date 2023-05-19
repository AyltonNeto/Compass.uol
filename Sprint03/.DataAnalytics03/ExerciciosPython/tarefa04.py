# Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

# Importante: Aplique a função range().

def isPrimo(num):
    if num % 2 == 0 and num != 2:
        return False
    elif num % 3 == 0 and num != 3:
        return False
    elif num % 5 == 0 and num != 5:
        return False
    elif num % 7 == 0 and num != 7:
        return False
    elif num % 11 == 0 and num != 11:
        return False
    else: return True

for i in range(2,101):
    if isPrimo(i):
        print (i)