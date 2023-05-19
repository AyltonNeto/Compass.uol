import pandas as pd

atores = pd.read_csv('actors.csv')

med_filmes = atores['Number of Movies'].mean()

print(f'A Média da coluna com os números de filmes é: {med_filmes}')