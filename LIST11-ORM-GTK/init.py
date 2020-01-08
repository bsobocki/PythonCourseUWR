from sqlalchemy import *

from connection import db_conn

def create_tables():
        try: 
            #connect to the database
            connection = db_conn()

            """ create tables """

            Table('event', connection.meta,
                Column('id', Numeric, primary_key=True),
                Column('title', String(60)),
                Column('start_time', TIMESTAMP, nullable=False),
                Column('end_time', TIMESTAMP, nullable=False),
                extend_existing=True
                )

            Table('person', connection.meta,
                Column('id', Numeric, primary_key=True),
                Column('name', String(100)),
                Column('email', String(60)),
                extend_existing=True
            )

            Table('person_at_event',  connection.meta,
                Column('person_id', Numeric, ForeignKey('person.id', ondelete='CASCADE')),
                Column('event_id', Numeric, ForeignKey('event.id', ondelete='CASCADE')),
                extend_existing=True
            )

            # Create the above tables
            connection.meta.create_all(connection.conn)
        except (Exception) as err: print(err)