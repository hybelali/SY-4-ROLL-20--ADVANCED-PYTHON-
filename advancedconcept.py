# Advanced Class Concepts in Python

# Parent Class
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance      # Encapsulation

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder :", self.holder)
        print("Balance        :", self.__balance)


# Child Class
class SavingsAccount(Account):
    def __init__(self, holder, balance, interest):
        super().__init__(holder, balance)
        self.interest = interest

    # Method Overriding
    def display(self):
        super().display()
        print("Interest Rate :", self.interest, "%")


# Another Child Class
class CurrentAccount(Account):
    def __init__(self, holder, balance, overdraft):
        super().__init__(holder, balance)
        self.overdraft = overdraft

    # Method Overriding
    def display(self):
        super().display()
        print("Overdraft Limit :", self.overdraft)
        