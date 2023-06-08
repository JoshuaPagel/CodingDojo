num1 = 42 # variable statement
num2 = 2.3 # variable statement
boolean = True #boolean
string = 'Hello World' #strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #type check
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #???
print(person['name']) #Log statement string
person['name'] = 'George' #list?
person['eye_color'] = 'blue' #list?
print(fruit[2]) #tuple

if num1 > 45: # For loop start
    print("It's greater") #log statement
else: #sequence
    print("It's lower") #log statement

if len(string) < 5: #for loop start
    print("It's a short word!") #log statement
elif len(string) > 15: #sequence
    print("It's a long word!") #log statement
else: #sequence
    print("Just right!") #log statement

for x in range(5): #for loop start
    print(x) #log statement
for x in range(2,5): #for loop start
    print(x) #log statement
for x in range(2,10,3): # for loop start
    print(x) #log statement
x = 0 #variable declaration
while(x < 5): #while loop
    print(x) #log statement
    x += 1 #start loop again until it reaches 4

pizza_toppings.pop() #??
pizza_toppings.pop(1) #return the second value?

print(person) #log statement
person.pop('eye_color') #return eye color
print(person) #log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #conditional
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional
        break #break

def print_hello_ten_times(): #?
    for num in range(10): #for loop start
        print('Hello') #log statement

print_hello_ten_times() #variable declaration

def print_hello_x_times(x): #?
    for num in range(x): #for loop start
        print('Hello') # log statement

print_hello_x_times(4) #function?

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #function, nothing in it
print_hello_x_or_ten_times(4) #function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)