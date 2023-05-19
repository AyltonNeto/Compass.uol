# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
# Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y,  e retorne 
# a subtração dos dois (resultados negativos são permitidos).

# Utilize os valores abaixo para testar seu exercício:
#   x = 4 
#   y = 5

# imprima:
#   Somando: 4+5 = 9
#   Subtraindo: 4-5 = -1

class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        self.sum = self.x + self.y
        return self.sum
    
    def sub(self):
        self.sub = self.x - self.y
        return self.sub

a = Calculo(4,5)
print(a.sum())
print(a.sub())