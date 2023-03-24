# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
# Dica: leia a documentação da função open(...)

arquivo = open('arquivo_texto.txt', 'r+')
dado = arquivo.readlines()
for linha in dado:
    print(f'{linha}', end='')

