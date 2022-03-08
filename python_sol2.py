# Solution 1

n = int(input('Enter no. of rows: '))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print(end='\n')

for i in range(n, 0, -1):
    for j in range(1, i):
        print('*', end='')
    print(end='\n')

# Write a Python program to reverse a word after accepting the input from the user.

string = input('Enter a string: ')

i = 1
while i <= len(string):
    print(string[-i], end='')
    i += 1
