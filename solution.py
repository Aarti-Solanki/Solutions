# solution 1

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')

# solution 2

f_name= input("Enter first name: ")
l_name = input("Enter last name: ")
name = f_name + ' ' +l_name
print(name[::-1])


# Solution 3

import math


def area(diameter):
    r = diameter/2
    volume = 4 / 3 * math.pi * r**3
    print(volume)


area(12)


