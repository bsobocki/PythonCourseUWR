import connection
from sqlalchemy import *

from connection import DataBase_Connection

class DataBase:
    conn = None
    person = None
    event = None
    person_at_event = None

    def __init__(self):
        self.conn = DataBase_Connection()
        tables = dict(self.conn.meta.tables)

        if 'person' in tables and 'event' in tables and 'person_at_event' in tables: 
              self.person = tables['person']
              self.event = tables['event']
              self.person_at_event = tables['person_at_event'] 


    def create_tables(self):
        try: 
            """ create tables """

            Table('event', self.conn.meta,
                Column('id', Numeric, primary_key=True),
                Column('title', String(60)),
                Column('start_time', TIMESTAMP, nullable=False),
                Column('end_time', TIMESTAMP, nullable=False),
                extend_existing=True
                )

            Table('person', self.conn.meta,
                Column('id', Numeric, primary_key=True),
                Column('name', String(100)),
                Column('email', String(60)),
                extend_existing=True
            )

            Table('person_at_event',  self.conn.meta,
                Column('person_id', Numeric, ForeignKey('person.id', ondelete='CASCADE')),
                Column('event_id', Numeric, ForeignKey('event.id', ondelete='CASCADE')),
                extend_existing=True
            )

            self.conn.meta.create_all(self.conn.conn)
            return "DataBase has tables: " + str(list(dict(self.conn.meta.tables).keys()))
        except (Exception) as err: return str(err)
    

    def get_rows_from_table(self, str_val):
        rows = []
        if str_val in ['person', 'event', 'person_at_event']:
            if str_val == "person":  
                rows = self.conn.conn.execute( self.person.select() )
            if str_val == 'event':
                rows = self.conn.conn.execute( self.event.select() )
            if str_val == 'person_at_event':
                rows = self.conn.conn.execute( self.person_at_event.select() )
            return rows
        else: raise Exception("Argument is not valid! Please call --write '{\"table\" :  \"person\", or \"event\", or \"person_at_event\" }'")