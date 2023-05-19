import pandas as pd

atores = pd.read_csv('actors.csv')

indice = atores['Average per Movie'].idxmax()
n_filmes = atores.loc[indice, 'Average per Movie']
ator_max = atores.loc[indice, 'Actor']

print(f'{ator_max} - Média por Filme: {n_filmes}')