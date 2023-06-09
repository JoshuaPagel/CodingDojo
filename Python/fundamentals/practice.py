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
def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
