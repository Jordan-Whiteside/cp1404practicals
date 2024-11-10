"""
Project management program.
Estimated: 5 hours
Actual: 5hr 19min
"""
from operator import attrgetter, itemgetter
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
            save_file(projects)
        elif choice == "D":
            display_project_completion_status(projects)
        elif choice == "F":
            display_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
            print(projects)
        elif choice == "U":
            update_project_with_error_checking(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_file(projects)
    print("Thank you for using custom-built project management software.")


def display_projects_by_date(projects):
    """Display projects after a certain date. Should sort by date."""
    # date_filter = convert_to_datetime_object("20/7/2022")
    date_filter = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
    filtered_projects = [project for project in projects if
                         convert_to_datetime_object(project.start_date) >= date_filter]
    for project in sorted(filtered_projects, key=attrgetter("start_date")):
        print(project)


def update_project_with_error_checking(projects):
    """Update chosen project with error checking."""
    for project_number, project in enumerate(projects):
        print(f"{project_number} {project}")
    project_choice = int(input("Project choice: "))
    while project_choice > len(projects) - 1:
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


def get_valid_number(prompt, low):
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt).strip())
            if number < low:
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

def save_file(projects):
    filename = input("Would you like to save to projects.txt? ").strip()
    if filename != "":
        save_projects(filename, projects)
    else:
        filename = DEFAULT_FILENAME
        save_projects(filename, projects)

def load_new_file():
    filename = input("filename (default - projects.txt): ").strip()
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
    name = get_valid_string("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    # Priority can't be lower than 1
    priority = get_valid_number("Priority: ", 1)
    # Cost can't be lower than $0
    cost_estimate = float(get_valid_number("Cost estimate: $", 0))
    completion_percentage = get_valid_percentage("Percentage complete: ")
    new_project = Project(name, start_date.strftime("%d/%m/%Y"), priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def get_valid_string(prompt):
    string = input(prompt).strip()
    while string == "":
        print("Invalid string must not be empty")
        string = input(prompt)
    return string


def get_valid_date(prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            date = input(prompt)
            date = convert_to_datetime_object(date)
            is_valid_input = True
        except ValueError:
            print("Invalid date")
    return date


def convert_to_datetime_object(string):
    date = datetime.datetime.strptime(string, "%d/%m/%Y").date()
    return date


def load_projects(filename):
    """Load projects from file. file attributes Name,Start Date,Priority,Cost Estimate,Completion Percentage"""
    # File attributes Name, Start Date, Priority, Cost Estimate, Completion Percentage
    records = []
    with open(filename) as in_file:
        # Skip field attributes on the first line.
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            record = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            records.append(record)
    return records


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w") as out_file:
        # Add field attributes on the first line.
        print(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        for project in projects:
            print(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                file=out_file)


main()
