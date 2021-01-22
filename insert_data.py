'''
This allows inserting data to the database
'''
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''
    Create a databse connectino to the SQLite database, specified by db_file
    :param db_file: database file
    :return: Connection object or None
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn

def create_log(conn, log):
    '''
    Create a new log into the logs table
    :param conn:
    :param log:
    :return: log id
    '''

    sql = '''INSERT INTO logs(date, workout)
            VALUES(?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, log)
    conn.commit()
    
    return cur.lastrowid

def create_gym(conn, gym):
    '''
    Create a workout to the gym table
    :param conn:
    :param gym:
    _return:
    '''
    sql = '''INSERT INTO gym(workout_id, move, sets, reps, weight, description)
            VALUES(?, ?, ?, ?, ?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, gym)
    conn.commit()

    return cur.lastrowid

def create_workout(conn, workout):
    '''
    Create a workout to the workout table
    :param conn:
    :param workout:
    :return:
    '''

    sql = '''INSERT INTO workout(workout_id, move, sets, reps, description)
            VALUES(?, ?, ?, ?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, workout)
    conn.commit()

    return cur.lastrowid

def create_run(conn, run):
    '''
    Create a workout to the run table
    :param conn:
    :param run:
    :return:
    '''

    sql = '''INSERT INTO run(workout_id, length_km, time_min, description)
            VALUES(?, ?, ?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, run)
    conn.commit()

    return cur.lastrowid

def create_other(conn, other):
    '''
    Create a workout to the workout table
    :param conn:
    :param other:
    :return:
    '''

    sql = '''INSERT INTO other(workout_id, sport, description)
            VALUES(?, ?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, other)
    conn.commit()

    return cur.lastrowid

def add_gym(conn, log_id):
    move = input('Insert move: ')    
    try:
        sets = int(input('Insert sets: '))
    except ValueError:
        sets = int(input('Insert sets (integer): '))

    try:
        reps = int(input('Insert reps: '))
    except ValueError:
        reps = int(input('Insert reps (integer): '))

    try:
        weight = float(input('Insert weight: '))
    except ValueError:
        weight = float(input('Insert weight (float): '))

    extra = input('Description?: ')

    gym = (log_id, move, sets, reps, weight, extra)
    create_gym(conn, gym)
    gym = ''

    #Create new workouts
    while True:
        add_workout = input('Add another move? (Y/N): ')
        if add_workout in ['Y', 'y']:
            move = input('Insert move: ')
                    
            try:
                sets = int(input('Insert sets: '))
            except ValueError:
                    sets = int(input('Insert sets (integer): '))

            try:
                reps = int(input('Insert reps: '))
            except ValueError:
                reps = int(input('Insert reps (integer): '))

            try:
                weight = float(input('Insert weight: '))
            except ValueError:
                weight = float(input('Insert weight (float): '))

            extra = input('Description?: ')

            gym = (log_id, move, sets, reps, weight, extra)
            create_gym(conn, gym)
            gym = ''

        elif add_workout in ['N', 'n']:
            print("Logging gym workout...")
            break


def add_workout(conn, log_id):
    move = input('Insert move: ')    
    try:
        sets = int(input('Insert sets: '))
    except ValueError:
        sets = int(input('Insert sets (integer): '))

    try:
        reps = int(input('Insert reps: '))
    except ValueError:
        reps = int(input('Insert reps (integer): '))

    extra = input('Description?: ')

    workout = (log_id, move, sets, reps, extra)
    create_workout(conn, workout)
    workout = ''

    #Create new workouts
    while True:
        add_workout = input('Add another move? (Y/N): ')
        if add_workout in ['Y', 'y']:
            move = input('Insert move: ')
                    
            try:
                sets = int(input('Insert sets: '))
            except ValueError:
                    sets = int(input('Insert sets (integer): '))

            try:
                reps = int(input('Insert reps: '))
            except ValueError:
                reps = int(input('Insert reps (integer): '))

            extra = input('Description?: ')

            workout = (log_id, move, sets, reps, extra)
            create_workout(conn, workout)
            workout = ''

        elif add_workout in ['N', 'n']:
            print("Logging workout...")
            break

def add_run(conn, log_id):    
    try:
        length = float(input('Insert length in km: '))
    except ValueError:
        length = float(input('Insert length in km (float): '))

    try:
        time = int(input('Insert time in mins: '))
    except ValueError:
        time = int(input('Insert time in mins (integer): '))

    extra = input('Description?: ')

    run = (log_id, length, time, extra)
    create_run(conn, run)
    run = ''

    #Create new workouts
    while True:
        add_workout = input('Add another run? (Y/N): ')
        if add_workout in ['Y', 'y']:
            try:
                length = float(input('Insert length in km: '))
            except ValueError:
                length = float(input('Insert length in km (float): '))

            try:
                time = int(input('Insert time in mins: '))
            except ValueError:
                time = int(input('Insert time in mins (integer): '))

            extra = input('Description?: ')

            run = (log_id, length, time, extra)
            create_run(conn, run)
            run = ''

        elif add_workout in ['N', 'n']:
            print("Logging run...")
            break

def add_other(conn, log_id):    
    sport = input('Insert sport: ')
    extra = input('Description?: ')

    other = (log_id, sport, extra)
    create_other(conn, other)
    other = ''

    #Create new workouts
    while True:
        add_workout = input('Add another kind of workout? (Y/N): ')
        if add_workout in ['Y', 'y']:
            sport = input('Insert sport: ')
            extra = input('Description?: ')

            other = (log_id, sport, extra)
            create_other(conn, other)
            other = ''

        elif add_workout in ['N', 'n']:
            print("Logging exercise...")
            break


def main():
    database = "workout.db"
    
    conn = create_connection(database) #Create a connection to the database
    with conn:
        #Create a new log to logs table
        date = input('Insert date (format YYYY-MM-DD): ')
        workout = input('Insert type of workout (Gym/Run/Workout/Other): ').lower()

        while workout not in ['gym', 'run', 'workout', 'other']:
            workout = input('Check your spelling and select from list [Gym, Run, Workout, Other]: ').lower()

        log = (date, workout)
        log_id = create_log(conn, log)

        # Fill correct table with values asked in respective functions

        if workout.lower() == 'workout':
            add_workout(conn, log_id)

        elif workout.lower() == 'gym':
            add_gym(conn, log_id)

        elif workout.lower() == 'run':
            add_run(conn, log_id)
        
        elif workout.lower() == 'other':
            add_other(conn, log_id)

        else:
            print('Logging out')

if __name__ == '__main__':
    main()
