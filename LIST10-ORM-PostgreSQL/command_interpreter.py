import sqlalchemy

from db_manipulator import db_manipulator
from database import database

def interpreter(command, val):
    """ 
        interprets commands: <command> in 
        for example:
            python3 main.py --add-person <values>
        @value = python dictionary
    """
    try:
        # connect to the database
        db = database()

        # create a new database manipulator
        db_manip = db_manipulator(db)

        # check command
        commands_actions = \
        {
            "--add-person": lambda : db_manip.add_person(val),
            "--add-event" : lambda : db_manip.add_event(val),
            "--add-person-at-event": lambda :db_manip.add_person_at_event(val),
            "--write": lambda : db.write(val),
            "--delete-person": lambda :db_manip.delete_person(val),
            "--delete-event": lambda :db_manip.delete_event(val)
        }

        # do action
        commands_actions[command]()

    except (Exception) as err: print(err)