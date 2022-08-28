"""
Banking application using OOP
Functions:
    * Withdrawal
    * Deposit
    * Balance
    * Write all transactions to a python file
"""

# Imports
from datetime import date

class Account:
    def __init__(self, initial_amount=0.00) -> None:
       self.balance = initial_amount
       self.name = ""

    def set_account_name(self, name):
        self.name = name

    def withdraw(self, amount):
        amount = self.validate_amount(amount)
        if amount > self.balance:
            print("Amount too large, you dont have that amount saved.")
            self.log("Failure: no withdrwal because amount bigger than current savings.\n")
        else:
            self.balance -= amount
            print("New balance:", self.balance)
            self.log(f"Success: {amount} has been removed. New balance: {self.balance}\n")
    
    def save(self, amount):
        amount = self.validate_amount(amount)
        self.balance += amount
        print("{} has been saved.\nNew balance: {}".format(amount, self.balance))
        self.log(f"Success: {amount} has been saved. New balance: {self.balance}\n")

    def info(self):
        print("Name:", self.name)
        print("Balance:", self.balance)
    
    def log(self, message):
        file = open('transactions.txt', 'a')
        log_str = "{}: {}".format(date.today(), message)
        file.write(log_str) 
        file.close()

    def validate_amount(self, amount):
        try:
            amount = float(amount)
            return amount
        except Exception as e:
            self.log(f"Falure: no valid amount passed. No action taken\n{e}")
            print("Enter valid amount")


def show_instructions():
    print("Welcome to the bank.")
    print("[1]: Set account name")
    print("[2]: Deposit")
    print("[3]: Withraw")
    print("[4]: Get account info")

def start():
    account = Account()
    while True:
        show_instructions()
        try:
            choice = int(input("Select action: "))
            if choice in [1, 2, 3, 4]:
                if choice == 1:
                    name = input("Enter an account holder's name: ")
                    account.set_account_name(name)
                if choice == 2:
                    amount = input("Enter amount to withdraw: ")
                    account.withdraw(amount)
                if choice == 3:
                    amount = input("Enter amount to deposit: ")
                    account.save(amount)
                if choice == 4:
                    account.info()
        except KeyboardInterrupt:
            print("Quiting...")
            break
        except ValueError:
            print("Please provide a lide choice")
            print("Quiting...")
            break


"""
Start the application here
"""
start()

