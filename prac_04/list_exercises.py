"""
CP1404 Practical - List exercises
"""

# Part 1 - Numbers:

numbers = []
for i in range(5):
    number = float(input("Enter number: "))
    numbers.append(number)
print(numbers)

print(f"The first number is {numbers[0]}.")
print(f"The last number is {numbers[-1]}.")
print(f"The smallest number is {min(numbers)}.")
print(f"The largest number is {max(numbers)}.")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.2f}.")

# Part 2 - Username Security Checker:

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob', 'eddie']
username = input("Enter username: ")
if username in usernames:
    print("Access granted.")
else:
    print("Access denied.")
