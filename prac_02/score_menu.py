"""Score function
Menu:
G get valid score (0 - 100)
P print result
S show stars
Q quit
"""


def main():
    score = get_valid_score()
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            get_valid_score()
        elif choice == "P":
            get_score_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid score.")
        print("Menu: ")
        choice = input("> ").upper()
    print("Farewell.")


def get_valid_score():
    score = int(input("Enter your score: "))
    return score


def get_score_result(score):
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
