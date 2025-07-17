"""CP1404 practical 7 project management program
Estimated time = 120 mins
Actual time = 60 mins
"""

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []
    print(MENU)
    menu_selection = input(">>> ").lower()
    while menu_selection != "q":
        if menu_selection == "l":
            filename = get_valid_input("Filename: ", "Filename cannot be blank")
            load_file(projects, filename)
        elif menu_selection == "s":
            filename = get_valid_input("Filename: ", "Filename cannot be blank")
            save_file(projects, filename)
        elif menu_selection == "d":
            display_projects(projects)
        elif menu_selection == "f":
            filter_projects_by_date(projects)
        elif menu_selection == "a":
            add_new_project(projects)
        elif menu_selection == "u":
            update_projects(projects)
        else:
            print("Invalid menu selection")
        print(MENU)
        menu_selection = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


def get_valid_input(prompt, error_message):
    """Get a valid input from the user."""
    user_input = input(prompt)
    while user_input == "":
        print(error_message)
        user_input = input(prompt)
    return user_input
