# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. 
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

import datetime

nome = input()
idade = int(input())

hoje = datetime.datetime.now()
cem_anos = (hoje.year-idade)+100

print(cem_anos)
