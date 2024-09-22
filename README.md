# 🏦 Bank Account Management System

## 📖 Description
Manage your bank accounts efficiently with this Python implementation. This project allows you to create various types of accounts, deposit, withdraw, transfer funds, and earn interest, all while providing user-friendly feedback.

## 🚀 Features
- **Multiple Account Types**: Choose from standard bank accounts, interest rewards accounts, and savings accounts tailored to your needs.
- **Transaction Management**: Effortlessly handle deposits, withdrawals, and fund transfers with built-in validations.
- **Robust Error Handling**: Stay informed with clear messages for insufficient funds and deposit limits.

## 💻 How to Use
1. Ensure you have Python installed on your system.
2. Run the main program using the command: `python main.py`
3. Follow the console instructions to create accounts and perform transactions.

## 📜 Classes

### BankAccount
- **Attributes**:
  - `name`: Name of the account holder.
  - `balance`: Current balance in the account.

- **Methods**:
  - `get_acc_balance()`: Displays the current balance.
  - `validate_deposit(amount)`: Validates the deposit amount against limits.
  - `deposit(amount)`: Adds money to the account.
  - `withdrawal(amount)`: Removes money from the account.
  - `transfer(amount, account)`: Transfers money to another account.

### InterestRewardsAcc
Inherits from `BankAccount` and includes interest earnings on your deposits!

### SavingsAcc
Inherits from `InterestRewardsAcc` and includes withdrawal fees.

## 🧠 Guide to Banking Functions
1. **Deposits**: Adding money to your account.
2. **Withdrawals**: Taking money out of your account.
3. **Transfers**: Moving money between accounts.
4. **Interest**: Earnings from your deposits.

> **Note**: If you want to learn more about banking functions, account types, or interest rates, please refer to the `guide_lines.txt` file for detailed explanations.


## 🛠️ Future Enhancements
- Implement a user interface for easier interaction.
- Add functionality for loan management.
- Expand error handling and validation features.

## 👨‍💻 Author
Khaled Soudy

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! Feel free to submit a Pull Request.

## 📞 Support
If you encounter any problems or have questions, please open an issue in the GitHub repository.

---
Happy banking and may your financial journey be prosperous! 💰
