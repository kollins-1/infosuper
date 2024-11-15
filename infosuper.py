class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        # Check if the withdrawal amount is greater than the available balance
        if amount > self.balance:
            return False, "Insufficient funds."
        elif amount <= 0:
            return False, "Please enter a valid amount."
        
        self.balance -= amount
        return True, f"Withdrawal of ${amount:.2f} was successful."

class ATM:
    def __init__(self):
        self.account = None

    def insert_card(self, account):
        self.account = account
        print(f"Welcome, Account #{account.account_number}!")

    def withdraw_cash(self):
        if not self.account:
            print("No card inserted. Please insert your card first.")
            return

        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Error: Please enter a valid numeric amount.")
            return

        success, message = self.account.withdraw(amount)
        if success:
            print(message)
            print(f"Remaining balance: ${self.account.check_balance():.2f}")
        else:
            print("Error:", message)

    def eject_card(self):
        if self.account:
            print(f"Thank you, Account #{self.account.account_number}. Please take your card.")
            self.account = None
        else:
            print("No card to eject.")

    def start(self):
        print("Welcome to the ATM. Please insert your card to begin.")
        while True:
            action = input("\nEnter command (insert, withdraw, eject, end): ").strip().lower()

            if action == "insert":
                if self.account:
                    print("Card is already inserted.")
                else:
                    account_number = input("Enter your account number: ")
                    balance = float(input("Enter your starting balance: "))
                    account = Account(account_number=account_number, balance=balance)
                    self.insert_card(account)

            elif action == "withdraw":
                self.withdraw_cash()

            elif action == "eject":
                self.eject_card()

            elif action == "end":
                if self.account:
                    self.eject_card()
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid command. Please enter 'insert', 'withdraw', 'eject', or 'end'.")

atm = ATM()
atm.start()
