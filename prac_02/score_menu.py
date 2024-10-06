"""
29/09/2024 - Score menu program
"""



def main():
    """Get a valid score and then display a menu"""
    score = get_valid_number("What was your score: ", 0, 100)
    menu = "- (G)et a valid score between 0-100\n- (P)rint results\n- (S)how stars\n- (Q)uit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("What is your score: ", 0, 100)
        elif choice == "P":
            result = determine_score_result(score)
            print(f"Your score is {result}")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_number(prompt, low, high):
    """Get a valid number between two numbers inclusive"""
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid number")
        number = int(input(prompt))
    return number


def determine_score_result(score):
    """Determine score status."""
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"

def print_asterisks(length):
    """Print Asterisks"""
    print("*" * length)

main()
