import database
import psycopg2.errors

class db_manipulator:
    db = None

    def __init__(self, database):
        self.db = database


    def _execute(self, clause):
        """ execute clause => create sqlalchemy.engine.result.ResultProxy object """
        return self.db.conn.conn.execute(clause)


    def add_person(self, val_dict):
        """ 
            Adds a new value to the table 'person' 
            @val is the value we want to add given as python dictionary:
                {'id':<id>, 'name':<name>, 'email':<email>}
        """
        try:
            if self.db.person is not None:
                # create sqlalchemy.sql.expression.Insert object
                clause = self.db.person \
                            .insert() \
                            .values(id=val_dict['id'], name=val_dict['name'], email=val_dict['email'])
            
                result = self.db.conn.conn.execute(clause)
                
                print('added person ' + val_dict['name'] + ' with id: ' + str(val_dict['id']))
                
                return result
            else: print("Something gone wrong! Person with parameters",val_dict,"were not added. May you should change parameters?\nNeeded data to add: [id, name, email]")
        
        except Exception: print("Sorry, you cannot add a new person with this parameters. \nPerson with this id is already exists or you do not give all needed data to add.\nNeeded data to add: [id, name, email]")
        except psycopg2.errors.UniqueViolation: print("Person with id",val_dict['id'],'is already exists. Please, change event id and add again.')


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
                
                print('added person ' + str(person[0][1]) + ' with id: ' + str(val['person_id']) + ' at event ' + str(event[0][1])+ ' with id: ' + str(val['event_id']))
                
                return result
            else: print("Something gone wrong! Person at event with parameters",val_dict,"were not added. May you should change parameters?\nNeeded data to add: [person_id, event_id]")
    
        except Exception as err: print(err,"Sorry, you cannot add this person to the event. \nThere is no person with given 'person_id', there is no event with given 'event_id' or you do not give all needed data to add.\nNeeded data to add: [person_id, event_id]")


    def add_event(self, val_dict):
        """ 
            Adds a new value to the table 'person' 
            @val is the value we want to add given as python dictionary:
                {'id':<id>, 'title':<title>, 'start_time':<start_time>, 'end_time':<end_time>}
        """
        try:
            if 'id' in val_dict and 'title' in val_dict and 'start_time' in val_dict and 'end_time' in vval_dictal:
                # create sqlalchemy.sql.expression.Insert object
                clause = self.db.event \
                            .insert() \
                            .values(id=val_dict['id'], title=val_dict['title'], start_time=val_dict['start_time'], end_time=val_dict['end_time'])
                result = self.db.conn.conn.execute(clause)
                
                print('added event ' + val_dict['title'] + ' with id: ' + str(val_dict['id']))
                
                return result
            else:
                print('Given argument:',val_dict,'is not a valid argument to add a new event. You should use argument looks like \'{"id":<numeric>, "title":<string>, "start_time":<timestamp>, "end_time":<timestamp>}\'')
        
        except Exception: print("Sorry, you cannot add this event. \nThere is an event with the given id or you do not give all needed data to add.\nNeeded data to add: [id, title, start_time, end_time]")
        except psycopg2.errors.UniqueViolation as err: print("Event with id",val['id'],'is already exists.\n Please, change event id and try again.')


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

                print('from now there is no person with',first_key,': ',val[first_key])
                
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

                    print('from now there is no person with',first_key,': ',val[first_key])
                    
                    return result
                else: print("Something gone wrong! Please meke sure that the given parameters are correct.")
            else: print("There is no event with parameter:",first_key)
        else: print("There is nothing to delete.")
            

        raise Exception("There is no event with given parameters.") 