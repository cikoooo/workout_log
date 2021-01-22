'''
For testing purposes
Pandas works nicely with sqlite
'''
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from insert_data import *

conn = sqlite3.connect('workout.db')
test = pd.read_sql('SELECT * FROM gym', conn)
paino = test['weight']
testi = pd.read_sql('SELECT * FROM logs', conn)
paiva = testi['date'][::-1]
paino = paino[:len(paiva)]

plt.plot(paiva, paino)
plt.show()

# insert_data() #tämä käynnistää insert_data:n

'''
Alkeellinen testi.
Piirtää sarjapainokehityksen, siten että päivä on x-akselilla ja paino y-akselilla.
Päivät järjestetty "luonnolliseen" järjestykseen
'''