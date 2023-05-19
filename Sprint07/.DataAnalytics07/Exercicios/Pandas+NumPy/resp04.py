import pandas as pd

atores = pd.read_csv('actors.csv')

count = atores['#1 Movie'].value_counts()
maior_freq = count.max()
mais_freq = count[count==maior_freq]

for filme, freq in mais_freq.items():
    print(f'{filme} - Frequência = {freq}')