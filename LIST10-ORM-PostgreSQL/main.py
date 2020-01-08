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
        try:
            # load json file as python dictionary
            val = json.loads(args[2])
        
            interpreter(command, val)
        except (Exception) as e: print("Argument is not valid! Please, give me valid JSON object as argument!\n",e)
        
    else: print("Please, give me more informations about what you want to do, because now i am not sure what i should do, so i am so sad :( )")
else: print("Please, give me more informations about what you want to do, because now i am not sure what i should do, so i am so sad :( )")
