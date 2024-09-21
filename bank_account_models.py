class BankAccount:
    def __init__(self, acc_name, initial_amount):
        self.name = acc_name
        self.balance = initial_amount
        
        # show a welcome message with details after each account creation
        print(f"✅ Account successfully created!\nAccount Name: {self.name}\t\t\tAccount Balance: ${self.balance:.2f}\n")
    
    
    def get_acc_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    
    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Completed Successfully ✅")
        self.get_acc_balance()
        
    
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\nWithdrawal Completed Successfully ✅")
            self.get_acc_balance()
        else:
            print(f"\nWithdrawal Interrupted ❌")
            print(f"\nAccount '{self.name}' only have a balance of ${self.balance:.2f}")
