# #1
# Create a function that accepts a number as an input.
# Return a new list that counts down by one,
# from the number (0th element) down to 0 (last element).

def countDown(x):
    listy = []
    for i in range(x,-1,-1):
        listy.append(i)
    return listy
print(countDown(5))

# #2
# Create a function that will receive a list with two numbers.
# Print the first and value and return the second .

def print_and_return(a,b):
    print(a)
    return b
print(print_and_return(1, 2))
# #3
# Create a function that accepts a list and returns the sum
# of the first value in the list plus the list's length.

def first_plus_length(myList):
    return(myList[0] + len(myList))
print(first_plus_length([1,2,3,4,5]))

# #4
# Write a function that accepts a list and 
# creates a new list containing only the values from 
# the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list.
# If the list has less than 2 elements, have the function return False

def values_greater_than_second(forthList):
    if len(forthList) < 2:
        return("false")
    outcome = []
    for i in range(0,len(forthList)):
        if forthList[i] > forthList[1]:
            outcome.append(forthList[i])
    print(len(outcome))

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3])) # works with the first part of the script


# #5
# Write a function that accepts two integers as parameters:
# size and value. The function should create and return a list
# whose length is equal to the given size, 
# and whose values are all the given value.

def length_and_value(size,value):
    output = []
    for i in range(0,size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
