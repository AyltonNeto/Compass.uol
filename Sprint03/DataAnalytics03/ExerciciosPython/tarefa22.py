# Crie uma classe chamada "Pessoa" com um atributo privado "nome" (representado como "__nome") e um atributo público "id". 
# Adicione duas funções à classe, uma para definir o valor de "nome" e outra para obter o valor de "nome". 
# Observe que o atributo "nome" deve ser privado e acessado somente através dessas funções.

# Para testar seu código use:
#    pessoa = Pessoa(0) 
#    pessoa.nome = 'Fulano De Tal'
#    print(pessoa.nome)

class Pessoa:
    def __init__(self, id):
        self.__nome = 'nome'
        self.id = id

    def nome(self):
        return
    
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)