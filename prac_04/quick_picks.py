"""
CP1404 Practical - Quick Picks program
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = get_valid_number()
    generate_quick_picks(number_of_quick_picks)


def get_valid_number():
    """Get a valid input from the user"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            is_valid_input = True
        except ValueError:
            print("Please enter a valid integer.")
    return number_of_quick_picks # No problem with potential undefined.


def generate_quick_picks(number_of_quick_picks):
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
