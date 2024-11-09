"""
Project management program.
Estimated: 5 hours
Actual:
"""

DEFAULT_FILE = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Load file then display menu. Will save file after quiting"""
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            print("Load projects")
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


main()
