class BankAccount:

    def __init__(self, name, balance, account_no):
        self.name = name
        self._balance = balance
        self.account_no = account_no

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            print("Balance must be a number")
            return

        if value < 0:
            print("Balance cannot be less than 0")
            return

        self._balance = value

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")

    def show_account_details(self):
        print(f"Owner: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Account No: {self.account_no}")


macrine = BankAccount(
    name="Macrine",
    balance=5000,
    account_no="11223344"
)

macrine.deposit(1000)
macrine.withdrawal(500)

macrine.show_account_details()