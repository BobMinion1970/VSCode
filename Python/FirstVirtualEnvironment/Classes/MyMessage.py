class MyMessage():
    _message = ""
    def __init__(self, theMessage):
        _message = theMessage
        print(self._message)

    def logMessage(self):
        print("LogMessage: " + self._message)        
    