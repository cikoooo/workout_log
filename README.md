# workout_log
Just a little project I made. I wanted to exercise how to create a database utilizing SQLite3 and Python.

create_db.py is used to create database.

create_tables.py is used to create two tables for the database, log and workout. Logs contain days I trained and type of workout, while workout (table) contains more information
of the workout (moves, sets, reps, weight...)

insert_data.py is used to insert workouts into the database.

Test:
Access SQL??? (cmd -> sqlite3 workout.db, should work but nope...)
.header on
.mode column

SELECT * FROM logs;
