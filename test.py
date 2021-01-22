'''
For testing purposes
Pandas works nicely with sqlite
'''
import pandas as pd
import sqlite3

conn = sqlite3.connect('workout.db')
test = pd.read_sql('SELECT * FROM gym WHERE "move" == "Penkki"', conn)
print(test.head())