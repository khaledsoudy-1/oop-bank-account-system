class BankAccount:
    def __init__(self, acc_name, initial_amount):
        self.name = acc_name
        self.balance = initial_amount
        
        # show a welcome message with details after each account creation
        print(f"✅ Account successfully created!\nAccount Name: {self.name}\t\t\tAccount Balance: ${self.balance}\n")


# Create an instance of the class
khaled = BankAccount("Khaled", "500")

# Get and print account name and balance
print(khaled.name)  # OUTPUT: Khaled
print(khaled.balance)  # OUTPUT: 500
