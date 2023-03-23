
arquivo = open('actors.csv')
dado = arquivo.readlines()
for linha in dado:
        campos = linha.strip().split(',')
        print(', '.join(campos))

