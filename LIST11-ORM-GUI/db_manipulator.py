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
            return str(er)
            return "Person with id" + str(self.person_id) + 'is already exists.\n \
                    Please, change event id and add again.'
        except Exception as e: 
            return str(e)
            return "Sorry, you cannot add a new person with this parameters. \nPerson with this id is already exists or you do not give all needed data to add.\n"


    def _check_name(self, name):
        return bool(re.match(r"[A-Z,a-z]+[A-Z,a-z,0-9]*", name))


    def _check_email(self, email):
        return bool(re.match(r"[A-Z,a-z]+[A-Z,a-z,0-9]*@[A-Z,a-z]+[A-Z,a-z,0-9]*\.[A-Z,a-z]+", email))


    def _get_max_person_id(self):
        max_person_id = Session().query(func.max(self.db.person.c.id)).scalar()
        if max_person_id is None: max_person_id = 0
        return max_person_id


    def _get_max_event_id(self):
        max_event_id = Session().query(func.max(self.db.event.c.id)).scalar()
        if max_event_id is None: max_event_id = 0
        return max_event_id


    def add_person_at_event(self, val):
        """ 
            Adds a new value to the table 'person_at_event' 
            @val is the value we want to add given as dictionary: 
                {'person_id':<person_id>, 'event_id':<event_id>} 
        """
        try:
            if self.db.person is not None:
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
                
                return 'Successfully added person ' + str(person[0][1]) + ' with id: ' + str(val['person_id']) + ' at event ' + str(event[0][1])+ ' with id: ' + str(val['event_id'])
                
            else: 
                return "Something gone wrong! \n" +  \
                        "Person at event with parameters" + str(val_dict) + "were not added.\n" + \
                        "May you should change parameters?\n"
    
        except Exception as err: 
            return "Sorry, you cannot add this person to the event. \n" + \
                    "There is no person with given 'person_id', there is no event with given 'event_id' or you do not give all needed data to add."


    def add_event(self, val_dict):
        """ 
            Adds a new value to the table 'person' 
            @val is the value we want to add given as python dictionary:
                {'title':<title>, 'start_time':<start_time>, 'end_time':<end_time>}
        """
        try:
            if 'id' in val_dict and 'title' in val_dict and 'start_time' in val_dict and 'end_time' in val_dict:

                event_id = self._get_max_event_id()

                clause = self.db.event \
                             .insert() \
                             .values(id=event_id, title=val_dict['title'], start_time=val_dict['start_time'], end_time=val_dict['end_time'])
                
                result = self.db.conn.conn.execute(clause)
                
                return 'added event ' + val_dict['title'] + '   '
            else:
                return 'Given argument:' + str(val_dict) + 'is not a valid argument to add a new event.'
        except psycopg2.errors.UniqueViolation as err: 
            return "Event with id" + str(self.event_id) + 'is already exists.\n Please, change event id and try again.'
        except Exception as e: 
            return "Sorry, you cannot add this event. \nThere is an event with the given id or you do not give all needed data to add.\nNeeded data to add: [title, start_time, end_time] "



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

                print('from now there is no person with',first_key,':',val[first_key])
                
                return result
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

                    print('from now there is no event with',first_key,':',val[first_key])
                    
                    return result
                else: print("Something gone wrong! Please meke sure that the given parameters are correct.")
            else: print("There is no event with parameter:",first_key)
        else: print("There is nothing to delete.")
            

        raise Exception("There is no event with given parameters.") 