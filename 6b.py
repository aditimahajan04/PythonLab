class InsufficientFundsException(Exception):
    pass

class InvalidAmountException(Exception):
    pass

class SavingsAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountException("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds for this withdrawal.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Account balance is {self.balance}.")

# Example usage:
account = SavingsAccount("123456", "Aditi Mahajan", 1000)
account.display_balance()

while True:
    try:
        action = input("Would you like to deposit (d) or withdraw (w) money? (Enter 'q' to quit): ").lower()
        if action == 'q':
            break
        elif action == 'd':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == 'w':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Invalid action. Please enter 'd' for deposit, 'w' for withdraw, or 'q' to quit.")
        account.display_balance()
    except (InvalidAmountException, InsufficientFundsException) as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
