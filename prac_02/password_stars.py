"""
Gets password then prints it in asterisks
"""


def main():
    """Ask the user for a password then print the length as asterisks."""
    minimum_password_length = 5
    password = get_password(minimum_password_length)
    print_asterisks(password)


def print_asterisks(password):
    """Print the length of the password as asterisks."""
    for i in password:
        print("*", end="")


def get_password(minimum_password_length):
    """Get a password from the user with error checking."""
    password = input(f"Password (At least {minimum_password_length} characters): ")
    while len(password) < minimum_password_length:
        print(f"Password must be at least {minimum_password_length} characters")
        password = input(f"Password (At least {minimum_password_length} characters): ")
    return password


main()
