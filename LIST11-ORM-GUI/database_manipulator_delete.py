import database
from db_manipulator import DataBase_Manipulator

import psycopg2.errors
from sqlalchemy.sql.expression import func 
from sqlalchemy.orm.session import Session
import re


class DataBase_Manipulator_Delete(DataBase_Manipulator):

    def __init__(self, database):
        super().__init__(database)


    def delete_person(self, val):
        """
            Deletes persons which have the same values as in the given parameters @val.
            For example: {"name":"Json"} -> delete all Jsons from database.
            You can give one parameter.
            If you give more than more parameter then the function will take only first one.
        """
        # if given value is not empty
        if len(val.keys()) > 0:
            first_key = list(val.keys())[0]
            # valid keys: 'id', 'name', 'email'
            if first_key in ['id', 'name', 'email']:
                # check first key
                if first_key=='id':
                    clause = self.db.person \
                                    .delete() \
                                    .where(self.db.person.c.id==val['id'])
                elif first_key=='name':
                    clause = self.db.person \
                                    .delete() \
                                    .where(self.db.person.c.name==val['name'])
                elif first_key=='email':
                    clause = self.db.person \
                                    .delete() \
                                    .where(self.db.person.c.email==val['email'])

                result = self.db.conn.conn.execute(clause)

                return 'from now there is no person with'+ str(first_key) + ':' + str(val[first_key])
                
            else: print("There is no person with parameter:",first_key)
        else: print("There is nothing to delete.")
        
        raise Exception("Argument is not valid!") 


    def delete_event(self, val):
        """
            Deletes persons which have the same values as in the given parameters @val.
            For example: {"name":"Json"} -> delete all Jsons from database.
            You can give one parameter.
            If you give more than more parameter then the function will take only first one.
        """
        # if given value is not empty
        if len(val.keys()) > 0:
            first_key = list(val.keys())[0]
            # valid keys: 'id', 'name', 'email'
            if first_key in ['id', 'title', 'start_time', 'end_time']:
                if self.db.event is not None:
                    # check first key
                    if first_key=='id':
                        clause = self.db.event \
                                        .delete() \
                                        .where(self.db.event.c.id==val['id'])
                    elif first_key=='title':
                        clause = self.db.event \
                                        .delete() \
                                        .where(self.db.event.c.title==val['title'])
                    elif first_key=='start_time':
                        clause = self.db.event \
                                        .delete() \
                                        .where(self.db.event.c.start_time==val['start_time'])
                    elif first_key=='end_time':
                        clause = self.db.event \
                                        .delete() \
                                        .where(self.db.event.c.end_time==val['end_time'])

                    result = self.db.conn.conn.execute(clause)

                    return 'from now there is no event with' + str(first_key) + ':' + str(val[first_key])      
                else: return "Something gone wrong! Please meke sure that the given parameters are correct."
            else: return "There is no event with parameter:" + str(first_key)
        else: return "There is nothing to delete."

        return "There is no event with given parameters."