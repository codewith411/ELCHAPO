class BankAccount:
    clients = 0
    bank_name = "Post Bank"

    def __init__(self, name, balance, account_no):
        self.name = name
        self._balance = balance
        self.account_no = account_no
        BankAccount.add_client()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            print("Ensure you pass a number for new balance")
            return

        if value < 0:
            print("Ensure new balance must not be less than 0")
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

    @staticmethod
    def calculate_interest(amount, year):
        rate = 10
        interest_per_year = amount * (rate / 100)
        interest_total = interest_per_year * year
        total = amount + interest_total

        print(f"Interest per year: {interest_per_year}")
        print(f"Total interest: {interest_total}")
        print(f"Total to pay after {year} years: {total}")

    @classmethod
    def add_client(cls):
        cls.clients = cls.clients + 1


john = BankAccount(
    name="John Mwangi",
    balance=5000,
    account_no="223344223"
)

samuel = BankAccount(
    name="Samuel",
    balance=3000,
    account_no="556677889"
)

print("Bank Name:", BankAccount.bank_name)
print("Total clients:", BankAccount.clients)

john.deposit(2000)
john.withdrawal(1000)

john.show_account_details()

BankAccount.calculate_interest(50000, 3)