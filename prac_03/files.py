"""
CP1404 - Practical
Files program: Using different techniques to read files
"""

FILENAME = "name.txt"
# 1.
out_file = open(FILENAME, "w")
name = input("What is your name? ")
print(f"{name}", file=out_file)
out_file.close()

# 2.
in_file = open(FILENAME, "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
