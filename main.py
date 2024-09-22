from bank_account_models import *

# Create an instance of the class
khaled = BankAccount("Khaled", 500)
sara = BankAccount("Sara", 1000)

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

# Make a Transfer
sara.transfer(1000, khaled)
# OUTPUT: Deposit Completed Successfully ✅

# Make another Transfer
sara.transfer(200, khaled)
# OUTPUT: Transfer Interrupted ❌: Sorry, account 'Sara' only has a balance of $0.00

#########################
# Create an Interest Rewards Account
john = InterestRewardsAcc("John", 5000)
# OUTPUT: ✅ Account successfully created!
# OUTPUT:  Account Name: John			Account Balance: $5000.00

# Make a Deposit
john.deposit(500)
# OUTPUT: Account 'John' balance = $5525.00

# Make a Transfer
john.transfer(1000, sara)
# OUTPUT: Account 'John' balance = $4525.00
# OUTPUT: Account 'Sara' balance = $1000.00
# OUTPUT: Transfer Completed Successfully ✅


#########################
# Create a Savings Account
messi = SavingsAcc("Messi", 8000)
# OUTPUT: ✅ Account successfully created!
# OUTPUT:  Account Name: Messi			Account Balance: $8000.00

# Make a Deposit
messi.deposit(1000)
# OUTPUT: Account 'Messi' balance = $9050.00

# Make a Transfer
messi.transfer(1000, sara)
# OUTPUT: Account 'Messi' balance = $8045.00
# OUTPUT: Account 'Sara' balance = $2000.00
# OUTPUT: Transfer Completed Successfully ✅
