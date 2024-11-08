"""My Guitars program."""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_file(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_file(filename):
    record = []
    # Each line in file contains the fields name,year,cost
    in_file = open(filename)
    for line in in_file:
        parts = line.strip().split(',')
        record.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    in_file.close()
    return record


main()
