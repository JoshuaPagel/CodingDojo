class BankAccount:
    def __init__(self,int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
    
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # def make_deposit(self, amount):
    #     self.account = BankAccount() + amount

    def make_deposit(self, amount):
        self.account.deposit(amount)
    
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)

    def balance_display(self):
        print(self.name)
        print(self.email)
        print(f"My interest rate is %{self.account.int_rate}")
        print(f"Current balance is ${self.account.balance}")


user1 = User("Josh", "jpagel@gmail.com")
user2 = User("Maddie", "Mjohnson@gmail.com")

user1.make_deposit(300)
user1.make_withdrawl(40)
user1.balance_display()

user2.balance_display()



# user1 = BankAccount(0.2, 400)
# user2 = BankAccount(0.1, 9000)


# user1.withdraw(30)
# user1.withdraw(44)
# user1.withdraw(61)
# user1.deposit(50)
# user1.yield_interest()
# user1.display_account_info()

# user2.withdraw(800)
# user2.deposit(600)
# user2.withdraw(720)
# user2.withdraw(666)
# user2.deposit(1000)
# user2.withdraw(20)
# user2.yield_interest()
# user2.display_account_info()
