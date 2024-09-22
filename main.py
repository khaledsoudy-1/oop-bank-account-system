from bank_account_models import *

# Create an instance of the class
khaled = BankAccount("Khaled", 500)

# Get and print account name and balance
print(khaled.name)  # OUTPUT: Khaled
print(khaled.balance)  # OUTPUT: 500

# Get account balance
khaled.get_acc_balance()  # OUTPUT: Account 'Khaled' balance = $500.00

# Make a Deposit
khaled.deposit(300)       # OUTPUT: Account 'Khaled' balance = $800.00

# Make a Withdrawal
khaled.withdrawal(300)    # OUTPUT: Account 'Khaled' balance = $500.00

# Make another Withdrawal
khaled.withdrawal(600)
# OUTPUT: Withdrawal Interrupted ❌: Sorry, account 'Khaled' only has a balance of $500.00

# Make another Deposit
khaled.deposit(200000)
# OUTPUT: Deposit Interrupted ❌: Deposits are limited between $10 : $10000