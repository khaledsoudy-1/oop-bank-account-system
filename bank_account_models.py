class BalanceException(Exception):
    pass


class DepositLimitException(Exception):
    pass


class BankAccount:
    MIN_LIMIT = 10
    MAX_LIMIT = 10000
    
    def __init__(self, acc_name, initial_amount):
        self.name = acc_name
        self.balance = initial_amount
        
        # show a welcome message with details after each account creation
        print(f"✅ Account successfully created!\nAccount Name: {self.name}\t\t\tAccount Balance: ${self.balance:.2f}\n")
    
    def get_acc_balance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}")
    
    def validate_deposit(self, amount):
        if self.MIN_LIMIT < amount < self.MAX_LIMIT:
            return
        raise DepositLimitException(f"Deposits are limited between ${self.MIN_LIMIT} : ${self.MAX_LIMIT}")
    
    def deposit(self, amount):
        try:
            self.validate_deposit(amount)
            self.balance += amount
            print("\nDeposit Completed Successfully ✅")
            self.get_acc_balance()
        
        except DepositLimitException as error:
            print(f"\nDeposit Interrupted ❌: {error}")
    
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        raise BalanceException(f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdrawal(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdrawal Completed Successfully ✅")
            self.get_acc_balance()
        
        except BalanceException as error:
            print(f"\nWithdrawal Interrupted ❌: {error}")
    
    def transfer(self, amount, account):
        try:
            print("\n========== Beginning Transfer... 🚀 ==========")
            
            # Ensure balance is sufficient before withdrawal to avoid incorrect transfers
            self.viable_transaction(amount)
            
            self.withdrawal(amount)
            account.deposit(amount)
            
            print("\nTransfer Completed Successfully ✅")
        
        except (BalanceException, DepositLimitException) as error:
            print(f"\nTransfer Interrupted ❌: {error}")
