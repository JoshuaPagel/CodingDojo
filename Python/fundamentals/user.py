class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        # print(f"{self.first_name}, {self.last_name}, {self.email}, {self.age}, {self.is_rewards_member}, {self.gold_card_points}")
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

User1 = User("Josh", "Pagel", "joshua.pagel20@gmail.com", 24)

User2 = User("Maddie", "Smith", "msith@gmail.com", 30)

User1.spend_points(50)
User1.display_info()

User2.enroll()
User2.spend_points(80)
User2.display_info()




# Enroll test
# User1.display_info()
# User1.enroll()
# User1.display_info()

# Spend points test
# User1.display_info()
# User1.spend_points(20)
# User1.display_info()