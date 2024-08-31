class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def add_funds(self, amount):
        if amount <= 0:
            print("You can't add 0 or less money")
        else:
            self.balance += amount
            print(f"Successfully added {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("You can't withdraw 0 or less money")
        elif self.balance < amount:
            print(f"Insufficient funds. You have {self.balance}, but tried to withdraw {amount}.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. New balance: {self.balance}")


def main():
    bank = BankAccount(0)
    bank.check_balance()

    try:
        deposit = float(input("Enter amount to deposit: "))
        bank.add_funds(deposit)
    except ValueError:
        print("Please enter a valid number for the deposit.")

    bank.check_balance()

    try:
        withdrawal = float(input("Enter amount to withdraw: "))
        bank.withdraw(withdrawal)
    except ValueError:
        print("Please enter a valid number for the withdrawal.")

    bank.check_balance()


if __name__ == "__main__":
    main()