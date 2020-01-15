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
        

    def write(self, val):
        rows = []
        if 'table' in val:
            if val['table'] in ['person', 'event', 'person_at_event']:
                if val['table'] == "person":  
                    rows = list(self.conn.conn.execute( self.person.select() ))
                    print( "There are {} persons. ".format(len(rows)) )
                    for row in rows: print( "{}, with email: {}".format(row[1], row[2]))

                if val['table'] == 'event':
                    rows = list(self.conn.conn.execute( self.event.select() ))
                    print( "There are {} events. ".format(len(rows)) )
                    for row in rows: print( "{}, starts at : {} and ends at {}".format(row[1], row[2], row[3]))

                if val['table'] == 'person_at_event':
                    persons_persons_at_events = self.person.join(self.person_at_event, self.person_at_event.c.person_id == self.person.c.id) 
                    persons_at_events = persons_persons_at_events.join(self.event, self.person_at_event.c.event_id == self.event.c.id)
                    rows = list( self.conn.conn.execute( select([self.person, self.event]).select_from(persons_at_events) ) )
                    for row in rows: print ("{} (id: {}) signed up for the event with title \"{}\" (id: {}) ".format(row[1], int(row[0]), row[4], int(row[3])))

                return True

        print("Argument is not valid! Please call --write '{\"table\" :  \"person\", or \"event\", or \"person_at_event\" }'")