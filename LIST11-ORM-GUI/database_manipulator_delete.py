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


    def delete_person_from_event(self, val):
        """ 
            Deletes the value from the table 'person_at_event' 
            \n@val is the value we want to delete given as dictionary\n: 
                {'person_id':<person_id>, 'event_id':<event_id>} 
        """
        try:
            if self.db.person is not None and self.db.event is not None and self.db.person_at_event is not None:
                clause = self.db.person_at_event \
                                .delete() \
                                .where(person_id=val['person_id'], event_id=val['event_id'])

                looking_for_person = self.db.person \
                                            .select() \
                                            .where(self.db.person.c.id==val['person_id'])

                looking_for_event = self.db.event \
                                            .select() \
                                            .where(self.db.event.c.id==val['event_id'])

                result = self.db.conn.conn.execute(clause)
                person = list(self.db.conn.conn.execute(looking_for_person))
                event = list(self.db.conn.conn.execute(looking_for_event))
                
                return 'Successfully removed:\n Person: ' + str(person[0][1]) + ' with id: ' + str(val['person_id']) + '\n From the event: ' + str(event[0][1])+ ' with id: ' + str(val['event_id'])
                
            else: 
                return "Something gone wrong! \n" +  \
                        "Person at event with parameters" + str(val_dict) + "were not added.\n" + \
                        "May you should change parameters?\n"
    
        except Exception as err: 
            return str(err) + "\nSorry, you cannot add this person to the event. \n" + \
                    "There is no person with given 'person_id', there is no event with given 'event_id' or you do not give all needed data to add."
