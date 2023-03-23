# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a lâmpada 
# estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

# liga(): muda o estado da lâmpada para ligada
# desliga(): muda o estado da lâmpada para desligada
# esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

# Para testar sua classe:
#   Ligue a Lampada
#   Imprima: A lâmpada está ligada? True
#   Desligue a Lampada
#   Imprima: A lâmpada ainda está ligada? False

class Lampada():
#    def __init__(self, ligada):
#        self.ligada = False

    def esta_ligada(self):
        if self.ligada == True:
            print('A lâmpada está ligada?', True)
        else: print('A lâmpada está ligada?', False)

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False
        
l1 = Lampada()
l1.liga()
l1.esta_ligada()
l1.desliga()
l1.esta_ligada()
