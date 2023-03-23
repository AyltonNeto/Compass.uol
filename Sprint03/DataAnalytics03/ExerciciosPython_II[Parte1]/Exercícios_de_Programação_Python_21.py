# Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, 
# porém, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.
# Imprima no console exatamente assim:
#    Pato
#    Voando...
#    Pato emitindo som...
#    Quack Quack
#    Pardal
#    Voando...
#    Pardal emitindo som...
#    Piu Piu

class Passaro():
    def voar(self):
        print('Voando...')
    
    def som(self):
        print('Passaro emitindo som...')

class Pato(Passaro):
    def especie(self):
        print('Pato')

    def som(self):
        print('Pato emitindo som...')
        print('Quack Quack')

class Pardal(Passaro):
    def especie(self):
        print('Pardal')
    
    def som(self):
        print('Pardal emitindo som...')
        print('Piu Piu')

piu1 = Pato()
piu1.especie()
piu1.voar()
piu1.som()

piu2 = Pardal()
piu2.especie()
piu2.voar()
piu2.som()