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
                                    workout text NOT NULL
                                    );'''

    sql_create_workout_table = '''CREATE TABLE IF NOT EXISTS workout (
                                    id integer PRIMARY KEY,
                                    workout_id integer NOT NULL,
                                    workout text NOT NULL,
                                    move text NOT NULL,
                                    sets integer,
                                    reps integer,
                                    weight float,
                                    extra text,
                                    FOREIGN KEY (workout_id) REFERENCES logs (id)
                                    );'''
    
    conn = create_connection(database) #Create a database connection

    #Create tables
    if conn is not None:
        create_table(conn, sql_create_logs_table)
        create_table(conn, sql_create_workout_table)

    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()
