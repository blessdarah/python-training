"""
Banking application using OOP
Functions:
    * Withdrawal
    * Deposit
    * Balance
    * Write all transactions to a python file
"""
class Account:
    def __init__(self, name: str, number: str, balance=0.0, log_file="transactions.txt") -> None:
        self.name = name
        self.number = number
        self.balance = balance
        self.log_file = log_file

    def credit(self, amount): # Credit = deposit
        if amount > 0:
            self.balance += amount
        else: 
            print("Cannot credit a negative number")
            print("Transaction cancelled")

    def debit(self, amount): # Debit = Withdrawal
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else: 
            print("Cannot debit beyond current balance")
            print("Transaction cancelled")

    def register_transaction(self, message: str):
       log_file = open(self.log_file, 'a') 
       log_file.write(message)
       log_file.close()

    
    def info(self):
        print("-----------Account info------------")
        print("Account name: ", self.name)
        print("Account number", self.number)
        print("Balance: ", self.balance)

def show_instructions():
    print("Welcome to the bank.")
    print("[1]: Set account name")
    print("[2]: Deposit")
    print("[3]: Withraw")
    print("[4]: Get account info")
    print("[5]: To quit")
   

