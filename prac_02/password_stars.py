minimum_password_length = 5
password = input(f"Password (At least {minimum_password_length} characters): ")
while len(password) < minimum_password_length:
    print(f"Password must be at least {minimum_password_length} characters")
    password = input(f"Password (At least {minimum_password_length} characters): ")
for i in password:
    print("*", end="")
