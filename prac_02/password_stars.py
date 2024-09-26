def main():
    """Ask the user for a password"""
    minimum_password_length = 5
    password = get_password(minimum_password_length)
    print_asterisks(password)


def print_asterisks(password):
    for i in password:
        print("*", end="")


def get_password(minimum_password_length):
    password = input(f"Password (At least {minimum_password_length} characters): ")
    while len(password) < minimum_password_length:
        print(f"Password must be at least {minimum_password_length} characters")
        password = input(f"Password (At least {minimum_password_length} characters): ")
    return password


main()
