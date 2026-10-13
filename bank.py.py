class InsufficientBalanceError(Exception):
    pass
class InvalidAmountError(Exception):
    pass
class DailyLimitExceededError(Exception):
    pass
class Bank:
    def __init__(self, id, name, balance):
        self.id, self.name, self.balance = id, name, balance
        self.daily_limit = 25000
        self.history = []
    def deposit(self):
        try:
            amount = int(input("Deposit your amount: "))
            if amount <= 0:
                raise InvalidAmountError("Amount should be greater than zero")
        except ValueError as e:
            print(e)
        except InvalidAmountError as e:
            print(e)
        else:
            self.balance += amount
            self.history.append(f"Deposited amount: {amount}")
            print("Amount deposited successfully")
    def withdraw(self):
        try:
            if self.daily_limit <= 0:
                raise DailyLimitExceededError("Daily limit exceeded")
            amount = int(input("Withdraw amount: "))
            if amount <= 0:
                raise InvalidAmountError("Amount should be greater than zero")
            if amount > self.daily_limit:
                raise DailyLimitExceededError("Withdrawal limit exceeded")
            if amount > self.balance:
                raise InsufficientBalanceError("You requested more than your actual balance")
        except ValueError as e:
            print(e)
        except InvalidAmountError as e:
            print(e)
        except DailyLimitExceededError as e:
            print(e)
        except InsufficientBalanceError as e:
            print(e)
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn: {amount}")
            print("Amount withdrawn successfully")
    def check_balance(self):
        return (f"Available Balance: {self.balance}")
    def transaction_history(self):
        print("\nTransaction History:")
        if self.history == []:
            print("No transactions found")
        else:
            for i in self.history:
                print(i)
# Create Account
id = int(input("Enter Account ID: "))
name = input("Enter Account Holder Name: ")
a1 = Bank(id, name, 0)
print("Account created successfully")
while True:
    print("\n------ ONLINE BANKING SYSTEM ------")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice from (1,2,3,4): "))
        if choice == 1:
            a1.deposit()
        elif choice == 2:
            a1.withdraw()
        elif choice == 3:
            print(a1.check_balance())
        elif choice == 4:
            a1.transaction_history()
            print(a1.check_balance())
            print("Thank you for using Ansu Bank.")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Please enter a valid number")