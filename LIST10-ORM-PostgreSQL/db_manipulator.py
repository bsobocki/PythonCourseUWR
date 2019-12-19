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
        if 'id' in val and 'name' in val and 'email' in val:
            # create sqlalchemy.sql.expression.Insert object
            clause = self.db.person \
                        .insert() \
                        .values(id=val['id'], name=val['name'], email=val['email'])
        
            return self._execute(clause)
        raise Exception("Arguments: " + str(list(val.keys())) + " are not valid or they are insufficient!")


    def add_person_at_event(self, val):
        """ 
            Adds a new value to the table 'person_at_event' 
            @val is the value we want to add given as dictionary: 
                {'person_id':<person_id>, 'event_id':<event_id>} 
        """
        if 'person_id' in val and 'event_id' in val:
            # create sqlalchemy.sql.expression.Insert object
            clause = self.db.person_at_event \
                        .insert() \
                        .values(person_id=val['person_id'], event_id=val['event_id'])
        
            return self._execute(clause)
        raise Exception("Arguments: " + str(list(val.keys())) + " are not valid or they are insufficient!")


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
            
                return self._execute(clause)
        except psycopg2.errors.
        raise Exception("Arguments: " + str(list(val.keys())) + " are not valid or they are insufficient!")


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
                return self._execute(clause)
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
                return self._execute(clause)
        raise Exception("Argument is not valid!") 