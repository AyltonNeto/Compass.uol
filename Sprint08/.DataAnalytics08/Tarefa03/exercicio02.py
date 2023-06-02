import pandas as pd

animais = ['gato', 'boto', 'sapo', 'quati', 'onça', 'iguana', 'jacaré', 'capivara', 'sucuri', 'papagaio', 'tucano', 'anta', 'lobo', 'rato', 'tamanduá', 'cutia', 'tatu', 'mico', 'jaguatirica', 'ariranha']
ordenar_animais = sorted(animais)
[print(animal) for animal in ordenar_animais]

df = pd.DataFrame(ordenar_animais, columns=["Animais"])
df.to_csv("animais.csv", index=False)