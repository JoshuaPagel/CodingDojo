# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# def be_cheerful(name="Mr. Nibbles", repeat=2):
#     print(f"Hey {name}\n" * repeat)

# be_cheerful("Josh")
# be_cheerful()
# be_cheerful(repeat=4,name="Billy Bob")




#debugging and multiplying
# def multiply(num_list, num):
#     for x in range(len(num_list)):
#         num_list[x] *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)




# Example of OOP

# class Vehicle:
#     def __init__(self, make, model, color, year, is_manuel, mileage):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.year = year
#         self.is_manuel = is_manuel
#         self.mileage = mileage
#         # print(self.model)

#     def display_info(self):
#         print(f"Make is {self.make}, model: {self.model} color: {self.color}") #F string example
#         print(self.make)
#         print(self.model) #Or type it out one at a time
#         print(self.color)
#         print(self.year)
#         print(self.is_manuel)
#         print(self.mileage)

#     def paint_job(self, color_chosen):
#         self.color = color_chosen
#         return self

# Changes Color on car
# vehicle1 = Vehicle("Nissan", "Skyline", "Sliver", 2021, True, 0)

#What will print
# vehicle1.display_info()
# print(vehicle1.paint_job("orange")) # prints none at the end (dont use print most likely)
# vehicle1.display_info()
# vehicle1.paint_job("blue")
# vehicle1.display_info()

# vehicle2 = Vehicle("Jaguar", "f-type", "orange", 1959, False, 400000)

# Will print both vehicles
# vehicle2.display_info()
# vehicle1.display_info()

# print(vehicle1.make)
# print(vehicle1.year)
# print(vehicle2.mileage)



#Advanced Methods for OOP
# class Shoe:
#     def __init__(self, brand, shoe_type, price):
#         self.brand = brand
#         self.shoe_type = shoe_type
#         self.price = price
#         # the status is set to true be default
#         self.in_stock = True
    
#     # Price of the item by that percentage
#     def on_sale_by_percent(self, percent):
#         self.price = self.price * (1 - percent)

# skater_shoe = Shoe("Vans", "Low-tops", 59.99)
# dress_shoe = Shoe("Jack and Jill", "Ballet Flats", 29.99)

# skater_shoe.on_sale_by_percent(0.2)
# dress_shoe.on_sale_by_percent(0.5)
# print(skater_shoe.price)
# print(dress_shoe.price)

# skater_shoe.on_sale_by_percent(0.2)

# The skater shoes go on sale byg 20% reduced price:
# skater_shoe.price = skater_shoe.price * (1 - 0.2)

# The dress shoes go on sale by 10% reduction:
# dress_shoe.price = dress_shoe.price * (1 - 0.1)

# The skater shoes go on sale again by another 10%
# skater_shoe.price = skater_shoe.price * (1 - 0.1)



# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Pass in all the values from the dictionary by their keys
# player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
# print(player_kevin.position) # prints small forward


#Class wednesday

# class Pet:
#     def __init__(self):
#         pass

#     @classmethod
#     def get_pet_by_name(cls, name):
        


def numbers(my_list):
    for num in my_list:
        if num % 2 != 0:
            print("hi")
        if num % 2 == 0:
            print("hello")
        if 9 > num > 5:
            print("hey")
        if num % 7 == 0:
            print("howdy")
        else:
            print("You have broken this game")

numbers([1,2,3,4,5,6,7,8,9,10])

item = {
    "color": "blue",
    "size" : "large"
}

# print(item["color"])


# for i in range(2, 16, 3):
#     print(i)

# def multiply(num_list,num):
#     for x in range(len(num_list)):
#         num_list[x] *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# output:
# >>>[10,20,50,80]

