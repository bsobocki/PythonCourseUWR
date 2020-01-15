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
            "--delete-event": lambda :db_manip.delete_event(val),
            "--help": print_help
        }

        # do action
        commands_actions[command]()

    except (Exception) as err: print("Something gone wrong! Please make sure that program argument is correct. If you need help, call --help.")

def print_help():
    print(
        "Hi! I'm your calendar. \
        \n You can add to my database: \
        \n - persons, by calling '--add-person' \
        \n - events, by calling '--add-event' \
        \n - person at event, by calling '--add-person-at-event'. \
        \n You can write contents of tables in my database: \
        \n - by calling '--write'. \
        \n You can delete from my database: \
        \n - persons, by calling '--delete-person' \
        \n - events, by calling '--delete-event'. \
        \n But calling one of arguments will be not enoguh! \
        \n You must give me parameters as JSON object!")