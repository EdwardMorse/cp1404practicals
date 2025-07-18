"""CP1404 practical 7 project management program
Estimated time = 120 mins
Actual time = 60 mins
"""

from project import ProjectManagement

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


def load_file(projects, filename):
    """Loads projects from the file."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = ProjectManagement(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        print(f"{filename} loaded.")


def save_file(contents, filename):
    """Saves projects to the file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for content in contents:
            print(
                f"{content.name}\t{content.start_date}\t{content.priority}\t{content.cost_estimate}\t{content.completion_percentage}",
                file=out_file)
        print(f"Projects are saved to {filename}.")


def display_projects(projects):
    """Display projects sorted by priority and completion percentage."""
    projects.sort()
    completed_projects = [project for project in projects if project.is_completed()]
    incompleted_projects = [project for project in projects if not project.is_completed()]
    print("Completed projects: ")
    for project in completed_projects:
        print(f"\t{project}")
    print("Incompleted projects: ")
    for project in incompleted_projects:
        print(f"\t{project}")


main()
