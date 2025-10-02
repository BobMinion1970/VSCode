class Customer:
    def __init__(self, id: str, last_name: str, first_name: str, account_id: int = 0):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.account_id_list = list()
        if account_id != 0:
            self.addAccount(account_id)

    def addAccount(self, account_id: int) ->None:
        self.account_id_list.append(account_id)

    def removeAccount(self, account_id: int) -> None:
        if len(self.account_id_list) == 0:
            raise IndexError("The account list is empty.")
        else:
            if account_id in self.account_id_list:
                self.account_id_list.remove(account_id)
            else:
                raise IndexError("There is no account with given id {}", account_id)
        
            
