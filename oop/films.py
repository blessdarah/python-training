from creditUnion import Account, show_instructions

def init():
    account = Account("none", "82302AD")
    show_instructions()
    try:
        choice = int(input("Select your action: ")) # expecting interger
        while(choice != 5):
            if choice == 1:
                new_acc_name = input("Enter an account name: ")
                account.name = new_acc_name
                print(f"Your account name has been changed to {account.name}")
            elif choice == 2:
                amount = int(input("Enter the amount to credit your account: "))
                account.credit(amount)
                account.register_transaction(f"Credit: {amount}\n")
            elif choice == 3:
                amount = int(input("Enter the amount to debit your account: "))
                account.debit(amount)
                account.register_transaction(f"Debit: {amount}\n")
            elif choice == 4:
                account.info()

            show_instructions()
            choice = int(input("Select your action: "))
    except Exception:
        print("Entered a wrong input value")
        print("Quiting application")
    

# Init the account class
init()

