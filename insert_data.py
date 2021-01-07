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

def create_workout(conn, workout):
    '''
    Create a workout to the workout table
    :param conn:
    :param workout:
    :return:
    '''

    sql = '''INSERT INTO workout(workout_id, workout, move, sets, reps, weight, extra)
            VALUES(?, ?, ?, ?, ?, ?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, workout)
    conn.commit()

    return cur.lastrowid

def main():
    database = "workout.db"
    
    conn = create_connection(database) #Create a connection to the database
    with conn:
        #Create a new log
        date = input('Insert date (format YYYY-MM-DD): ')
        workout = input('Insert type of workout (chest/legs/back...): ')
        log = (date, workout)
        log_id = create_log(conn, log)

        # TODO tämä kaikki omaksi funktioksi? Näyttäisi paremmalta
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

        extra = input('More info?: ')

        workout = (log_id, workout, move, sets, reps, weight, extra)
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

                try:
                    weight = float(input('Insert weight: '))
                except ValueError:
                    weight = float(input('Insert weight (float): '))

                extra = input('More info?: ')

                workout = (log_id, workout, move, sets, reps, weight, extra)
                create_workout(conn, workout)
                workout = ''

            elif add_workout in ['N', 'n']:
                print("Logging workout...")
                break


        
if __name__ == '__main__':
    main()
