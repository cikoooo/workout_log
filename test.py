'''
For testing purposes
Pandas works nicely with sqlite
'''
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import datetime
from datetime import date
from insert_data import *

conn = sqlite3.connect('workout.db')

'''
Alkeellinen testi.
Piirtää sarjapainokehityksen, siten että päivä on x-akselilla ja paino y-akselilla.
Päivät järjestetty "luonnolliseen" järjestykseen
'''

painot = pd.read_sql('SELECT AVG(weight) FROM gym WHERE move = "Penkki" GROUP BY workout_id', conn)
paivat = pd.read_sql('SELECT logs.date FROM logs INNER JOIN gym ON logs.id = gym.workout_id WHERE gym.move ="Penkki" GROUP BY logs.id', conn)
print(len(painot), len(paivat))
plt.scatter(paivat['date'], painot['AVG(weight)'])
plt.show()

# insert_data() #tämä käynnistää insert_data:n
