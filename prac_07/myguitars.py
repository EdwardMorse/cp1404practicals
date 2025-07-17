"""
Practical 7 - CP1404
My guitars program
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r+") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    add_guitars(guitars)
    display_guitars(guitars)
    save_file(guitars)


def add_guitars(guitars):
    """Add guitar to the list of guitars."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"{add_guitar} added.")
        name = input("Name: ")


def display_guitars(guitars):
    """Display guitars oldest to newest."""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def save_file(contents):
    """Saves guitars to a file."""
    with open(FILENAME, "w", encoding="utf-8") as out_file:
        for content in contents:
            print(f"{content}", file=out_file)


main()
