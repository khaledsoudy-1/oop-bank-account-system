class BankAccount:
    def __init__(self, acc_name, initial_amount):
        self.name = acc_name
        self.balance = initial_amount
        
        # show a welcome message with details after each account creation
        print(f"✅ Account successfully created!\nAccount Name: {self.name}\t\t\tAccount Balance: ${self.balance:.2f}\n")
    
    
    def get_acc_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    
    