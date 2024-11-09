"""My Guitars program."""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars file then display, user can add guitars, saves guitars back to file"""
    guitars = load_file(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    add_new_guitars(guitars)
    save_guitars(FILENAME, guitars)


def add_new_guitars(guitars):
    """Add new guitars untill name is blank."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")


def load_file(filename):
    """Load guitar file."""
    record = []
    # Each line in file contains the fields name,year,cost
    in_file = open(filename)
    for line in in_file:
        parts = line.strip().split(',')
        record.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    in_file.close()
    return record


def save_guitars(filename, guitars):
    """Save guitars to file"""
    out_file = open(filename, 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
