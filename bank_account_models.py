class BalanceException(Exception):
    """Exception raised for insufficient balance in the account."""
    pass


class DepositLimitException(Exception):
    """Exception raised for deposit amounts outside the allowed limits."""
    pass


class BankAccount:
    MIN_LIMIT = 10                           # Minimum deposit limit
    MAX_LIMIT = 10000                        # Maximum deposit limit
    
    def __init__(self, acc_name, initial_amount):
        self.name = acc_name                 # Set account name
        self.balance = initial_amount        # Set initial balance
        
        # Show a welcome message after account creation
        print(f"\n✅ Account successfully created!\nAccount Name: {self.name}\t\t\tAccount Balance: ${self.balance:.2f}\n")
    
    def get_acc_balance(self):
        """Print the current balance of the account."""
        print(f"Account '{self.name}' balance = ${self.balance:.2f}")
    
    def validate_deposit(self, amount):
        """Validate the deposit amount against the limits."""
        if self.MIN_LIMIT < amount < self.MAX_LIMIT:
            return               # Amount is valid
        raise DepositLimitException(f"Deposits are limited between ${self.MIN_LIMIT} : ${self.MAX_LIMIT}")
    
    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        try:
            self.validate_deposit(amount)               # Check if deposit is within limits
            self.balance += amount                      # Increase the balance
            print("\nDeposit Completed Successfully ✅")
            self.get_acc_balance()                      # Show updated balance
        
        except DepositLimitException as error:
            print(f"\nDeposit Interrupted ❌: {error}")
    
    def viable_transaction(self, amount):
        """Check if there is sufficient balance for a transaction."""
        if self.balance >= amount:
            return                # Balance is sufficient
        raise BalanceException(f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdrawal(self, amount):
        """Withdraw the specified amount from the account."""
        try:
            self.viable_transaction(amount)              # Check if withdrawal is possible
            self.balance -= amount                       # Deduct the amount from balance
            print("\nWithdrawal Completed Successfully ✅")
            self.get_acc_balance()                       # Show updated balance
        
        except BalanceException as error:
            print(f"\nWithdrawal Interrupted ❌: {error}")
    
    def transfer(self, amount, account):
        """Transfer the specified amount to another account."""
        try:
            print("\n========== Beginning Transfer... 🚀 ==========")
            
            # Ensure balance is sufficient before withdrawal to avoid incorrect transfers
            self.viable_transaction(amount)              # Check balance for the transfer
            
            self.withdrawal(amount)                      # Perform the withdrawal
            account.deposit(amount)                      # Deposit to the target account
            
            print("\nTransfer Completed Successfully ✅")
        
        except (BalanceException, DepositLimitException) as error:
            print(f"\nTransfer Interrupted ❌: {error}")


class InterestRewardsAcc(BankAccount):
    Interest_rate = 0.05  # Interest rate for the savings account
    
    def deposit(self, amount):
        """Override: Deposit the specified amount into the savings account, including interest."""
        try:
            self.validate_deposit(amount)  # Validate deposit limits
            
            # Increase balance by the deposit amount plus interest on that amount
            self.balance += (amount + self.Interest_rate * amount)
            
            print("\nDeposit Completed Successfully ✅")
            self.get_acc_balance()  # Show updated balance
        
        except DepositLimitException as error:
            print(f"\nDeposit Interrupted ❌: {error}")


class SavingsAcc(InterestRewardsAcc):
    Fees = 5            # Fixed fee for withdrawals
    
    def withdrawal(self, amount):
        """Override: Withdraw the specified amount from the savings account, including a fee."""
        try:
            self.viable_transaction(amount + self.Fees)  # Check if withdrawal is possible
            
            # Deduct the withdrawal amount plus the fee
            self.balance -= (amount + self.Fees)
            
            print("\nWithdrawal Completed Successfully ✅")
            self.get_acc_balance()  # Show updated balance
        
        except BalanceException as error:
            print(f"\nWithdrawal Interrupted ❌: {error}")