"""Score function
Menu:
G get valid score (0 - 100)
P print result
S show stars
Q quit
"""


def main():
    """Perform menu options."""
    score = get_valid_score()
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            get_score_result(score)
            print(f"The score of {score} is {get_score_result(score)}.")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid input.")
        print("Menu: ")
        choice = input("> ").upper()
    print("Farewell.")


def get_valid_score():
    """Get a valid score."""
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid. Your score must be between 0 and 100")
        score = int(input("Enter score: "))
    return score


def get_score_result(score):
    """Get the score result."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print stars length of score"""
    print("*" * score)


main()
