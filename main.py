from bank_account_models import *

# Create an instance of the class
khaled = BankAccount("Khaled", 500)

# Get and print account name and balance
print(khaled.name)  # OUTPUT: Khaled
print(khaled.balance)  # OUTPUT: 500

# Get account balance
khaled.get_acc_balance()  # OUTPUT: Account 'Khaled' balance = $500.00

