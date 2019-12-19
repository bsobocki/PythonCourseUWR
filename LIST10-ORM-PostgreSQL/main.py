import sqlalchemy
import psycopg2
import sys
import json

from init import create_tables
from command_interpreter import interpreter

# get program arguments
args = sys.argv

# check command
if len(args) > 1 :
    command = args[1]

    # database initialize 
    if command == '--init': create_tables()

    # do action
    elif len(args) > 2:
        # load json file as python dictionary
        val = json.loads(args[2])

        interpreter(command, val)
