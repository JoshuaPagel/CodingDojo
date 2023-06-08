#1
for i in range(0,150):
    print(i)
#2
for i in range(5,1000,5):
    print(i)
#3
for i in range(1,100):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
#4
count = 0
for i in range(0,500000):
    if(i % 2 !=0):
        count += i
print(count)
#5
count = 2018
while count > 0:
    count -= 4
    if count > 0:
        print(count)
#6
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum + 1):
    if i % mult == 0:
        print(i)
