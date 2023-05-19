# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

import os
from dotenv import load_dotenv
import Classes.MyMessage as mym


################################ Functions #####################################
def testVenv():
    _message1 = mym.MyMessage(theMessage="This is an error message!", error=True)
    _message2 = mym.MyMessage(theMessage="This is an info message.")

def myLogin():
    load_dotenv()
    
    _username: str
    _password: str
    _retVal: bool = False
    
    _username = input("User name: ")
    _password = input("Password: ")
    _storeduser = os.getenv("MYUSERNAME")
    _storedpassword = os.getenv("PASSWORD")
    
    if _username != _storeduser:
        print("Please provide correct username")
        
    elif _password != _storedpassword:
        print("Please provide correct password")
    else:
        _retVal = True
    
    return _retVal
    
def main():
    _login: bool = False
    
    _login = myLogin()
    if _login:
        testVenv()
    
################################# Main ########################################
main()
