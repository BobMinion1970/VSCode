class Account:
    def __init__(self, account_id: int, customer_id: str, balance: float) -> None:
        self.account_id : int = account_id
        self.balance : float = balance
        self.customer_id : str = customer_id
        self.lock = False

    def add_to_balance(self, deposit: float) -> float:
        if self.lock == False: 
            self.balance += deposit
        else:
            raise AttributeError("Account is locked")
        
        return self.balance
    
    def debit_from_account(self, debit: float) -> float:
        if self.lock == False:
            self.balance -= debit
        else: 
            raise AttributeError("Account is locked")
   
        return self.balance
    
    def lock_account(self, lock: bool) -> bool: 
        self.lock = lock
        return self.lock
