"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Convert celsius to fahrenheit and vise versa."""
    menu = f"C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit_from_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius_from_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius_from_fahrenheit(fahrenheit):
    """Calculate celsius from fahrenehit."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit_from_celsius(celsius):
    """Calculate fahrenheit from celsius."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
