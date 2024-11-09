"""
Project management program.
Estimated: 5 hours
Actual:
"""
from prac_07.project import Project

DEFAULT_FILE = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Load file then display menu. Will save file after quiting"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} from {DEFAULT_FILE}")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            print("Load from new file")
        elif choice == "S":
            print("Save projects")
        elif choice == "D":
            print("Display projects")
        elif choice == "F":
            print("Filter projects by date")
        elif choice == "A":
            print("Add new project")
        elif choice == "U":
            print("Update project")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Quit")


def load_projects(filename):
    records = []
    with open(filename) as in_file:
        in_file.readline()  #
        for line in in_file:
            parts = line.strip().split("\t")
            record = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            records.append(record)
    return records


main()
