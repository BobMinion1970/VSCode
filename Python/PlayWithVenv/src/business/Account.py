class Account():
    def __init__(self, account_id: int, customer_id: str, balance: float) -> None : 
        self.account_id = account_id
        self.balance = balance
        self.customer_id = customer_id

    def add_to_balance(self, deposit: float) -> float:
        self.balance += deposit
        return self.balance
