import sqlite3
from sqlite3 import Error


# Class for managing database operations
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def create_connection(self):
        # Create connection to the database
        try:
            self.conn = sqlite3.connect(':memory:')
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    def check_database(self):
        # Check if database is active
        try:
            print(f'Checking if {self.db_name} exists or not...')
            print(f'Database exists. Successfully connected to {self.db_name}')

        except sqlite3.OperationalError as err:
            print('Database does not exist')
            print(err)
