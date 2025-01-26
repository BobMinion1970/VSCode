# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error
#import pdb

import os
import sys
import sqlite3
import logging
from pathlib import Path

try: 
    _mainpath = os.getcwd()
    sys.path.append(_mainpath + '\\Database')
    sys.path.append(_mainpath + '\\Business')
    sys.path.append(_mainpath +  '\\GUIPWD')      
except FileNotFoundError:
    pass   

import DB
import mainMenue
 
logger = logging.getLogger(__name__)
logging.basicConfig(filename='PlayWithDatabase.log', encoding='utf-8', level=logging.DEBUG)
  
def main() -> None:
    
    try:
        db = DB.DBSingleton.instance()  # sqlite3.connect(Path('D:/Develop/Projects/TAT/VSCode/Python/PlayWithDatabase/PlayWithDatabase.db'))
        if db:
            db.initDB()        
    except sqlite3.Error as e:    
        logger.debug(e)
        print("Database connection failed. Check whether database <PlayWithDatabase.db> exists in application folder")
    
    
    mainMenue.mainmenue(db)
    
main()
