"""
Password function
"""


def main():
    password = get_valid_password()
    print_hidden_password(password)


def get_valid_password():
    """Return a valid password."""
    password = get_password()
    return password

# Refactored 4 lines.
def get_password():
    """Return a valid password."""
    password = input("Enter password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long")
        password = input("Enter password: ")
    return password


def print_hidden_password(password):
    """Print hidden password of length asterisk"""
    length = len(password)
    print("*" * length)


main()
