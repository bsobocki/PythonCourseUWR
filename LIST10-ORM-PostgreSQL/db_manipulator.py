import database
import psycopg2.errors

class db_manipulator:
    db = None

    def __init__(self, database):
        self.db = database


    def _execute(self, clause):
        """ execute clause => create sqlalchemy.engine.result.ResultProxy object """
        return self.db.conn.conn.execute(clause)


    def add_person(self, val):
        """ 
            Adds a new value to the table 'person' 
            @val is the value we want to add given as python dictionary:
                {'id':<id>, 'name':<name>, 'email':<email>}
        """
        try:
            # create sqlalchemy.sql.expression.Insert object
            clause = self.db.person \
                        .insert() \
                        .values(id=val['id'], name=val['name'], email=val['email'])
        
            result = self.db.conn.conn.execute(clause)
            
            print('added person ' + val['name'] + ' with id: ' + str(val['id']))
            
            return result
        
        except Exception: print("Sorry, you cannot add a new person with this parameters. \nPerson with this id is already exists or you do not give all needed data to add.\nNeeded data to add: [id, name, email]")
        except psycopg2.errors.UniqueViolation: print("Person with id",val['id'],'is already exists. Please, change event id and add again.')


    def add_person_at_event(self, val):
        """ 
            Adds a new value to the table 'person_at_event' 
            @val is the value we want to add given as dictionary: 
                {'person_id':<person_id>, 'event_id':<event_id>} 
        """
        try:
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
    
        except Exception as err: print(err,"Sorry, you cannot add this person to the event. \nThere is no person with given 'person_id', there is no event with given 'event_id' or you do not give all needed data to add.\nNeeded data to add: [person_id, event_id]")


    def add_event(self, val):
        """ 
            Adds a new value to the table 'person' 
            @val is the value we want to add given as python dictionary:
                {'id':<id>, 'title':<title>, 'start_time':<start_time>, 'end_time':<end_time>}
        """
        try:
            if 'id' in val and 'title' in val and 'start_time' in val and 'end_time' in val:
                # create sqlalchemy.sql.expression.Insert object
                clause = self.db.event \
                            .insert() \
                            .values(id=val['id'], title=val['title'], start_time=val['start_time'], end_time=val['end_time'])
                result = self.db.conn.conn.execute(clause)
                
                print('added event ' + val['title'] + ' with id: ' + str(val['id']))
                
                return result
        
        except Exception: print("Sorry, you cannot add this event. \nThere is an event with the given id or you do not give all needed data to add.\nNeeded data to add: [id, title, start_time, end_time]")
        except psycopg2.errors.UniqueViolation as err: print("Event with id",val['id'],'is already exists.\n Please, change event id and add again.')


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

        raise Exception("Argument is not valid!") 