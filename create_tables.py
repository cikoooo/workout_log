'''
Creating necessary tables for database
'''

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    '''
    Create a database connection to the SQLite database, specified by db_file
    :param db_file: database file
    :return: Connection object or None
    '''

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    '''
    Create a table from sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    '''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    
    except Error as e:
        print(e)

def main():
    database = "workout.db"
    
    sql_create_logs_table = '''CREATE TABLE IF NOT EXISTS logs (
                                    id integer PRIMARY KEY,
                                    date DATE NOT NULL,
                                    workout VARCHAR(16) NOT NULL
                                    );'''

    sql_create_gym_table = '''CREATE TABLE IF NOT EXISTS gym (
                                    id integer PRIMARY KEY,
                                    workout_id integer,
                                    workout VARCHAR(16) DEFAULT 'Gym',
                                    move VARCHAR(32) NOT NULL,
                                    sets integer,
                                    reps integer,
                                    weight float,
                                    description VARCHAR(255),
                                    FOREIGN KEY (workout_id) REFERENCES logs(id)
                                    );'''

    sql_create_workout_table = '''CREATE TABLE IF NOT EXISTS workout (
                                    id integer PRIMARY KEY,
                                    workout_id integer,
                                    workout VARCHAR(16) DEFAULT 'Workout',
                                    move VARCHAR(32) NOT NULL,
                                    sets integer,
                                    reps integer,
                                    description VARCHAR(255),
                                    FOREIGN KEY (workout_id) REFERENCES logs(id)
                                    );'''
    
    sql_create_run_table = '''CREATE TABLE IF NOT EXISTS run (
                                    id integer PRIMARY KEY,
                                    workout_id integer,
                                    workout VARCHAR(16) DEFAULT 'Run',
                                    length_km float NOT NULL,
                                    time_min integer,
                                    description VARCHAR(255),
                                    FOREIGN KEY (workout_id) REFERENCES logs(id)
                                    );'''

    sql_create_other_table = '''CREATE TABLE IF NOT EXISTS other (
                                    id integer PRIMARY KEY,
                                    workout_id integer,
                                    workout VARCHAR(16) DEFAULT 'Other',
                                    sport VARCHAR(32) NOT NULL,
                                    description VARCHAR(255),
                                    FOREIGN KEY (workout_id) REFERENCES logs(id)
                                    );'''

    conn = create_connection(database) #Create a database connection

    #Create tables
    if conn is not None:
        create_table(conn, sql_create_logs_table)
        create_table(conn, sql_create_gym_table)
        create_table(conn, sql_create_workout_table)
        create_table(conn, sql_create_run_table)
        create_table(conn, sql_create_other_table)
        print('Tables created')

    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()
