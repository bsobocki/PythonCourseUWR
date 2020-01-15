import sqlalchemy
import psycopg2
from sqlalchemy import *

class DataBase_Connection:
    conn = None,
    meta = None,
    
    def __init__(self):
        self.connect()

    def connect(self, user='pyrole', password='pyrole', db='calendar', host='localhost', port='5432'):
        """ connect to the DataBase """

        # PostgreSQL url that helps connecting to the database
        # postgresql://pyrole:pyrole@localhost:5432/calendar
        url = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, db)

        # The return value of create_engine() is our connection object
        self.conn = sqlalchemy.create_engine(url, client_encoding='utf8')

        # Bind the connection to MetaData()
        self.meta = sqlalchemy.MetaData(bind=self.conn, reflect=True)