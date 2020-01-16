import database
from db_manipulator import DataBase_Manipulator

import psycopg2.errors
from sqlalchemy.sql.expression import func 
from sqlalchemy.orm.session import Session
import re


class Database_Manipulator_Add(DataBase_Manipulator):

    def __init__(self, database):
        super().__init__(database)


    def add_person(self, val_dict):
        """ 
            Adds a new value to the table 'person' 
            @val is the value we want to add given as python dictionary:
                {'name':<name>, 'email':<email>}
        """
        try:
            if self.db.person is not None:
                if not self._check_name(val_dict["name"]) : 
                    return  "Wrong name! \n" + \
                            "The correct name contains only big and low letters and numbers."
                if not self._check_email(val_dict["email"]): 
                    return "Wrong email!\n\n" + \
                           "Email Template:\n[letters and numbers] @ [letters and numbers] . [letters]"
                
                person_id = self._get_max_person_id()

                clause = self.db.person \
                             .insert() \
                             .values(id=person_id, name=val_dict['name'], email=val_dict['email'])
            
                result = self.db.conn.conn.execute(clause)
                    
                return 'Successfully added person ' + str(val_dict['name']) + "  "
            else: 
                return "Something gone wrong!\n\
                        Person with parameters" + str(val_dict) + "were not added. \n\
                        May you should change parameters?"

        except psycopg2.errors.UniqueViolation as er: 
            return "Person with id" + str(self.person_id) + 'is already exists.\n \
                    Please, change person id and try again.'
        except Exception as e: 
            return "Sorry, you cannot add a new person with this parameters. \nPerson with this id is already exists or you do not give all needed data to add.\n"


    def _check_name(self, name):
        return bool(re.match(r"[A-Z,a-z]+[A-Z,a-z,0-9,\.]*", name))


    def _check_email(self, email):
        return bool(re.match(r"[A-Z,a-z]+[A-Z,a-z,0-9,\.]*@[A-Z,a-z]+[A-Z,a-z,0-9,\.]*\.[A-Z,a-z]+", email))


    def _get_max_person_id(self):
        max_person_id = Session().query(func.max(self.db.person.c.id)).scalar()
        max_person_id = max_person_id+1 if not max_person_id is None else 0 
        return max_person_id


    def _get_max_event_id(self):
        max_event_id = Session().query(func.max(self.db.event.c.id)).scalar()
        max_event_id = max_event_id+1 if not max_event_id is None else 0
        return max_event_id


    def add_person_at_event(self, val):
        """ 
            Adds a new value to the table 'person_at_event' 
            @val is the value we want to add given as dictionary: 
                {'person_id':<person_id>, 'event_id':<event_id>} 
        """
        try:
            if self.db.person is not None and self.db.event is not None and self.db.person_at_event is not None:
                # create sqlalchemy.sql.expression.Insert object
                clause = self.db.person_at_event \
                            .insert() \
                            .values(person_id=val['person_id'], event_id=val['event_id'])

                looking_for_person = self.db.person \
                                            .select() \
                                            .where(self.db.person.c.id==val['person_id'])

                looking_for_event = self.db.event \
                                        .select() \
                                        .where(self.db.event.c.id==val['event_id'])

                result = self.db.conn.conn.execute(clause)
                person = list(self.db.conn.conn.execute(looking_for_person))
                event = list(self.db.conn.conn.execute(looking_for_event))
                
                return 'Successfully added:\n Person: ' + str(person[0][1]) + ' with id: ' + str(val['person_id']) + '\n For event: ' + str(event[0][1])+ ' with id: ' + str(val['event_id'])
                
            else: 
                return "Something gone wrong! \n" +  \
                        "Person at event with parameters" + str(val_dict) + "were not added.\n" + \
                        "May you should change parameters?\n"
    
        except Exception as err: 
            return str(err) + "\nSorry, you cannot add this person to the event. \n" + \
                    "There is no person with given 'person_id', there is no event with given 'event_id' or you do not give all needed data to add."


    def add_event(self, val_dict):
        """ 
            Adds a new value to the table 'person' 
            @val is the value we want to add given as python dictionary:
                {'title':<title>, 'start_time':<start_time>, 'end_time':<end_time>}
        """
        try:
            if self.db.event is not None:
                if 'title' in val_dict and 'start_time' in val_dict and 'end_time' in val_dict:
                    event_id = self._get_max_event_id()

                    clause = self.db.event \
                                .insert() \
                                .values(id=event_id, title=val_dict['title'], start_time=val_dict['start_time'], end_time=val_dict['end_time'])
                    
                    result = self.db.conn.conn.execute(clause)
                    
                    return 'Successfully added event ' + val_dict['title'] + '.   '
                else:
                    return 'Given arguments:' + str(val_dict) + 'are not a valid arguments to add a new event.'
        except psycopg2.errors.UniqueViolation as err: 
            return "Event with id" + str(self.event_id) + 'is already exists.\n Please, change event id and try again.'
        except Exception as e: 
            return "Sorry, you cannot add this event. \n Problem: " + str(e)
