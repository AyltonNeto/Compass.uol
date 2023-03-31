# A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. 
# Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas
# (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. 
# Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar 
# o maior valor dentre eles.

# Veja o exemplo:
#    Entrada
#    operadores = ['+','-','*','/','+']
#    operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

# Aplicar as operações aos pares de operandos
#    [ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 

# Obter o maior dos valores: 12
# Na resolução da atividade você deverá aplicar as seguintes funções:
#    max
#    zip
#    map

def operacao(tupla, str):
    if str == '+':
        return tupla[0]+tupla[1]
    elif str == '-':
        return tupla[0]-tupla[1]
    elif str == '*':
        return tupla[0]*tupla[1]
    elif str == '/':
        return tupla[0]/tupla[1]
    elif str == '%':
        return tupla[0]%tupla[1]
    else: return 0

def calcular_valor_maximo(operadores,operandos):
    y = list(zip(operandos,operadores))
    x = list(map(lambda x: operacao(x[0],x[1]), y))
    return(max(x))

op1 = ['+','-','*','/','+']
op2 = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(op1,op2))