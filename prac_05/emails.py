"""
Emails program
Estimated: 50min
Actual:
"""

email = input("Email: ")
email_to_name = {}
while email != "":
    name = " ".join(email.split("@")[0].title().split("."))
    is_name = input(f"Is your name {name}? (Y/n) ").lower()
    if is_name == "y" or is_name == "":
        email_to_name[email] = name
    else:
        # Name could be empty
        name = input("Name: ").title()
        email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
