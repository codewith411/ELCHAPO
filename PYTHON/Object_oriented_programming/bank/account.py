class BankAccount:

    def __init__(self, name, balance, no):
        self.name = name
        self.balance = balance
        self.no = no

    # Getter
    def get_balance(self):
        return self.balance

    # Deposit
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    # Withdrawal
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    # Show account details
    def show_account_details(self):
        print(f"Account Name: {self.name}")
        print(f"Account Number: {self.no}")
        print(f"Balance: {self.balance}")


# Create account
account = BankAccount("Macrine", 5000, "ACC001")

# Deposit
account.deposit(2000)

# Withdrawal
account.withdrawal(1000)

# Show balance
print(f"Current Balance: {account.get_balance()}")

# Show account
account.show_account_details()