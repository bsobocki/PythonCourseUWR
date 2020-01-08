import connection
from sqlalchemy import *

from connection import db_conn

class database:
    conn = None
    person = None
    event = None
    person_at_event = None

    def __init__(self):
        # connect to the database
        self.conn = db_conn()

        # get the database tables 
        tables = dict(self.conn.meta.tables)
        
        # check if database is initialized
        if 'person' in tables: self.person = tables['person']
        if 'event' in tables: self.event = tables['event']
        if 'person_at_event' in tables: self.person_at_event = tables['person_at_event'] 
        

    def get_rows_from_table(self, val_dict):
        rows = []
        if 'table' in val_dict:
            if val_dict['table'] in ['person', 'event', 'person_at_event']:
                if val_dict['table'] == "person":  
                    rows = self.conn.conn.execute( self.person.select() )
                if val_dict['table'] == 'event':
                    rows = self.conn.conn.execute( self.event.select() )
                if val_dict['table'] == 'person_at_event':
                    rows = self.conn.conn.execute( self.person_at_event.select() )
                return rows
        else: raise Exception("Argument is not valid! Please call --write '{\"table\" :  \"person\", or \"event\", or \"person_at_event\" }'")