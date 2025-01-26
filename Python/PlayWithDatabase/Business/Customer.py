import datetime

class Customer:
    def __init__(self, id, firstname, lastname, birthday) -> None:
        self._id = id
        self._firstname = firstname
        self._lastname = lastname
        self._birthday = birthday

    def age(self) -> str: 
        retval : str = ''
        if isinstance(self._birthday, str):
            bdsplit = self._birthday.split(".")
            month = datetime.date.today().month
            year = datetime.date.today().year
            if month > int(bdsplit[1]):
                age = year - int(bdsplit[0])
            else:
                age = year - int(bdsplit[0]) - 1
                retval = str(age)
            
            return retval
                                   