import pandas as pd

atores = pd.read_csv('actors.csv')

indice = atores['Number of Movies'].idxmax()
n_filmes = atores.loc[indice, 'Number of Movies']
ator_max = atores.loc[indice, 'Actor']

print(f'{ator_max} - {n_filmes} filmes')