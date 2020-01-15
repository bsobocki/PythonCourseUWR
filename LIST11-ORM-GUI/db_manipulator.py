import database
import psycopg2.errors
from sqlalchemy.sql.expression import func 
from sqlalchemy.orm.session import Session
import re


class DataBase_Manipulator:
    db = None,

    def __init__(self, database):
        self.db = database


    def _execute(self, clause):
        """ execute clause => create sqlalchemy.engine.result.ResultProxy object """
        return self.db.conn.conn.execute(clause)


    def create_database_content(self):
        return self.db.create_tables()
