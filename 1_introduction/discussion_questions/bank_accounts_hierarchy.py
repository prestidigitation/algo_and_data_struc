class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
            return self.balance
        else:
            print("Can't withdraw. You have negative funds!")
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class CheckingAccount(BankAccount):
    pass


class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, rate, withdrawals_this_year=0):
        super().__init__(account_number, balance)
        self.interest_rate = rate
        self.withdrawals_this_year = withdrawals_this_year

    def add_interest(self):
        interest = super().get_balance() * self.interest_rate / 100
        super().deposit(interest)

    def withdraw(self, amount):
        if self.withdrawals_this_year >= 6:
            print("Can't withdraw. Maximum number of yearly withdrawals has been reached!")
            return self.balance
        elif self.balance > 0:
            self.balance -= amount
            self.withdrawals_this_year += 1
            return self.balance
        else:
            print("Can't withdraw. You have negative funds!")
            return self.balance

    def get_withdrawal_number(self):
        return self.withdrawals_this_year
