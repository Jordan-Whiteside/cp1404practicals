"""
Guitars program
Predicted: 20min
Actual: 25min
"""
from prac_06.guitar import Guitar

guitars = []
print("My guitars")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_to_add = Guitar(name, year, cost)
    guitars.append(guitar_to_add)
    print(guitar_to_add, "added.")
    name = input("Name: ")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

if guitars:  # lists, strings and other collections are False when empty, True when non-empty
    print("These are my guitars:")
    for i, guitar_to_add in enumerate(guitars, 1):
        vintage_string = ""
        if guitar_to_add.is_vintage():
            vintage_string = " (vintage)"
        print(
            f"Guitar {i}: {guitar_to_add.name:>20} ({guitar_to_add.year}), worth ${guitar_to_add.cost:10,.2f}{vintage_string}")
else:
    print("No guitars")
