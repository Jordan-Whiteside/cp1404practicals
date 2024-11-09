"""
Project management program.
Estimated: 5 hours
Actual:
"""
from operator import attrgetter

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
            projects = load_new_file(projects)
        elif choice == "S":
            print("Save projects")
        elif choice == "D":
            display_project_completion_status(projects)
        elif choice == "F":
            print("Filter projects by date")
        elif choice == "A":
            add_new_project(projects)
            print(projects)
        elif choice == "U":
            print("Update project")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Quit")


def load_new_file(projects):
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
    records = []
    with open(filename) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            record = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            records.append(record)
    return records


main()
