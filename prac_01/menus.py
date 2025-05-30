"""
CP1404 Practical 1
Menus program
"""

name = input("What is your name? ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}.")
    elif choice == "G":
        print(f"Goodbye {name}.")
    else:
        print("Invalid choice.")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
