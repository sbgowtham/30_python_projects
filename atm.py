class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        return f"Your account balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."

# Create an instance of the ATM
atm = ATM()
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print(atm.check_balance())
    elif choice == '2':
        amount = float(input("Enter the deposit amount: "))
        print(atm.deposit(amount))
    elif choice == '3':
        amount = float(input("Enter the withdrawal amount: "))
        print(atm.withdraw(amount))
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
