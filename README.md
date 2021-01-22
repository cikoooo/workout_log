# workout_log
Just a little project I made. I wanted to exercise how to create a database utilizing SQLite3 and Python.

create_db.py is used to create database.

create_tables.py is used to create five tables for the database: logs, gym, workout, run and other.
Tables contain following:
- logs: id, date, type of workout
- gym: id, workout_id (foreign key to logs(id)), workout (default gym), move, sets, reps, weight, description
- workout: id, workout_id (foreign key to logs(id)), workout (default workout), move, sets, reps, description
- run: id, workout_id (foreign key to logs(id)), workout (default run), length in km, time in minutes, description
- other: id, workout_id (foreign key to logs(id)), workout (default other), sport, description

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
