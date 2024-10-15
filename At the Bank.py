class Bank:
    def __init__ (self, name, account_owner, account_balance):
        self.name = name
        self.account_owner = account_owner
        self.account_balance = int(account_balance)

    def deposit (self, amount ):
        if amount > 0:
            self.account_balance += amount
            print(f"The amount {amount} has been deposited. The new balance is {self.account_balance}")

    def show_balance(self):
        print(f"You current balance is {self.account_balance}.")

    def withdrawal (self, amount):
        if amount > 0 < 500:
         self.account_balance -= amount
         print(f"Thanks, you have withdrawn {amount}. The new balance is now {self.account_balance} ")
        else:
         print(f"Please enter a deposit amount less than {amount}, daily amount limit is 500")


test_bank = Bank("HSBC", "Dere", 345)


test_bank.show_balance()