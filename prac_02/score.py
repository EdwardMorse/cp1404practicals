"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Get the valid score and display the result."""
    score = float(input("Enter score: "))
    print(determine_score_result(score))
    random_score = random.randint(0, 100)
    print(f"The random score of {random_score} is {determine_random_score(random_score)}.")

def determine_score_result(score):
    """Determine the result category of the valid score."""
    while score < 0 or score > 100:
        print("Invalid. Your score must be between 0 and 100")
        score = float(input("Enter score: "))
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def determine_random_score(random_score):
    """Return a random valid score."""
    if random_score >= 90:
        return "Excellent"
    elif random_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
