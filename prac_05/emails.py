"""
CP1404 Practical
E-mails - program
Estimate: 18 mins
Actual: 35 mins
"""


def main():
    """Creates a dictionary, emails_to_names"""
    email_to_name = {}
    email = input("Enter e-mail: ")
    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n)")
        if name_confirmation != "Y" and name_confirmation != "":
            name = input("What is your name? ")
        email_to_name[email] = name
        email = input("Enter e-mail: ")

    max_length = max(len(name) for name in email_to_name.values())
    for email, name in email_to_name.items():
        print(f"{name:{max_length}} ({email})")


def get_name_from_email(email):
    """Finds the predicted name based on the e-mail address"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()

# testing emails:
# eddie.morse@my.jcu.edu.au
# zach.morse@my.jcu.edu.au
# charlotte.taylor@my.jcu.edu.au
