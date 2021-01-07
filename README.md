# workout_log
Just a little project I made. I wanted to exercise how to create a database utilizing SQLite3 and Python.

create_db.py is used to create database.

create_tables.py is used to create two tables for the database, log and workout. Logs contain days I trained and type of workout, while workout (table) contains more information
of the workout (moves, sets, reps, weight...)

insert_data.py is used to insert workouts into the database.

Test:
    THIS IF NOT STARTED BY ANACONDA
    '''
    SQLITE3 in \anaconda3\Library\bin
    from there .\sqlite3 and ".open c:\\users\\Nico\\Documents\\tty\\ohjelmointi\\workout_log\\workout.db"
    '''

    Easier with anaconda:
    sqlite3 workout.db

    check tables:
    .tables

    styling, optional:
    {
    .header on
    .mode column
    }

    And see all the logs:
    SELECT * FROM logs;
