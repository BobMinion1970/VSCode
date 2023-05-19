# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from pip._vendor.colorama import init, Fore
class MyMessage():
    _message: str = ""
    def __init__(self, theMessage: str, error: bool = False):
        self._message = theMessage
        if error:
            print(Fore.RED + theMessage)
        else:
            print(Fore.WHITE + self._message)

    def logMessage(self):
        print("LogMessage: " + self._message)      
    