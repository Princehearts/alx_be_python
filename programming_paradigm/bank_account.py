class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit an amount to the account."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Withdraw an amount from the account if funds are sufficient."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
