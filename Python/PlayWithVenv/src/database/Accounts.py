from ..business import Account


class Accounts:
    def __init__(self):
        self.accounts: list = []

    def add_account(self, account: Account.Account) -> None:
        self.accounts.append(account)

    def remove_account(self, id) -> None:
        for delaccount in self.accounts:
            if delaccount.id == id:
                self.accounts.remove(delaccount)

    def get_deposit_sum_of_customer(self, customer_id: str) -> float:
        sum: float = 0.0
        for account in self.accounts:
            if account.customer_id == customer_id:
                sum += account.balance

        return sum
