# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
#   a lista recebida dividida em 3 partes iguais. 

# Teste sua implementação com a lista abaixo:
#   lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tam = len(lista)//3

a = lista[0:tam]
b = lista[4:2*tam]
c = lista[8:3*tam]

print(a,b,c)
