"""
Project management program.
Estimated: 5 hours
Actual:
"""
from operator import attrgetter
import datetime

from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Load file then display menu. Will save file after quiting"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} from {DEFAULT_FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_new_file()
        elif choice == "S":
            # TODO: Save projects
            print("Save projects")
        elif choice == "D":
            display_project_completion_status(projects)
        elif choice == "F":
            # TODO: Filer projects by date
            print("Filter projects by date")
        elif choice == "A":
            add_new_project(projects)
            print(projects)
        elif choice == "U":
            update_project_with_error_checking(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Quit")


def update_project_with_error_checking(projects):
    """Update chosen project with error checking."""
    for project_number, project in enumerate(projects):
        print(f"{project_number} {project}")
    project_choice = int(input("Project choice: "))
    while project_choice > len(projects) -1:
        print("Invalid project")
        project_choice = int(input("Project choice: "))
    print(f"Record {projects[project_choice]}")
    new_percentage = input("New percentage: ")
    if new_percentage != "":
        is_valid_input = False
        while not is_valid_input:
            try:
                new_percentage = int(new_percentage)
                if new_percentage < 0 or new_percentage > 100:
                    print("Invalid percentage, must be between 0 and 100")
                projects[project_choice].completion_percentage = new_percentage
                is_valid_input = True
            except ValueError:
                print("Invalid percentage")
    new_priority = input("New priority: ")
    if new_priority != "":
        is_valid_input = False
        while not is_valid_input:
            try:
                new_priority = int(new_priority)
                if new_priority < 1:
                    print("Invalid priority")
                projects[project_choice].priority = new_priority
                is_valid_input = True
            except ValueError:
                print("Invalid priority")

def get_valid_number(prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt).strip())
            if number < 1:
                print("Invalid priority")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input (not an integer)")
    return number


def get_valid_percentage(prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            percentage = int(input(prompt).strip())
            if percentage < 0 or percentage > 100:
                print("Invalid percentage, must be between 0 and 100")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input (not an integer)")
    return percentage


def modify_completion_percentage(project):
    new_percentage = int(input("New percentage: "))
    if new_percentage != "":
        project.completion_percentage = new_percentage


def load_new_file():
    filename = input("filename: ").strip()
    if filename != "":
        projects = load_projects(filename)
    else:
        filename = DEFAULT_FILENAME
        projects = load_projects(filename)
    print(f"Loaded {len(projects)} from {filename}")
    return projects


def display_project_completion_status(projects):
    """Display all projects based on completion status"""
    sorted_projects = sorted(projects, key=attrgetter("priority"))
    incomplete_projects = [project for project in sorted_projects if project.is_incomplete()]
    complete_projects = [project for project in sorted_projects if project.is_complete()]
    print("Incomplete projects:")
    display_projects(incomplete_projects)
    print("Complete projects:")
    display_projects(complete_projects)


def display_projects(projects):
    """Display projects."""
    for project in projects:
        print(f"  {project}")


def add_new_project(projects):
    """Add new project object to list."""
    print("Let's add a new project")
    # TODO: Add error checking
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percentage complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def load_projects(filename):
    """Load projects from file. file attributes Name,Start Date,Priority,Cost Estimate,Completion Percentage"""
    # File attributes Name, Start Date, Priority, Cost Estimate, Completion Percentage
    records = []
    with open(filename) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            record = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            records.append(record)
    return records


main()

# date.strftime("%d/%m/%Y")
# date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
# import datetime
#
# date_string = input("Date (dd/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))
