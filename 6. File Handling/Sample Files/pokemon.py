import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#imports csv data and stores as 
df = pd.read_csv('pokemon.csv')

#Use Boolean indexing to filter for Water pokemon
fairy_pokemon = df[df['Type 1'] == "Fairy"]

#print the fairy pokemon Df
print(fairy_pokemon)

#create a scatterplot showing fairy pokemon speed and HP
plt.scatter(fairy_pokemon['HP'],fairy_pokemon['Speed'])
plt.title('Fairy Pokemon Scatterplot')
plt.xlabel('Hitpoints')
plt.ylabel('Speed')
plt.savefig('Fairy_Pokemon.png')
