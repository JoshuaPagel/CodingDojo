class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = .01
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
    
    # Classmethod attempt
    # @classmethod
    # def all_balances(cls):
    #     sum = 0
    #     for account in cls.all_balances:
    #         sum += account.balance
    #     return sum


user1 = BankAccount(400)
user2 = BankAccount(9000)

user1.withdraw(30)
user1.withdraw(44)
user1.withdraw(61)
user1.deposit(50)
user1.yield_interest()
user1.display_account_info()

user2.withdraw(800)
user2.deposit(600)
user2.withdraw(720)
user2.withdraw(666)
user2.deposit(1000)
user2.withdraw(20)
user2.yield_interest()
user2.display_account_info()


# Testing
# user1.withdraw(200)

# user1.deposit(100)

# user1.yield_interest()

# user1.display_account_info()

