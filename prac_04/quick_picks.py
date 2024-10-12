"""Module 4 - Quick Picks"""

from random import randint

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
NUMBER_OF_RANDOM_NUMBERS_IN_LINE = 6

def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick_numbers = []
        generate_quick_pick_numbers(quick_pick_numbers)
        display_quick_pick_numbers(quick_pick_numbers)

def generate_quick_pick_numbers(quick_pick_numbers):
    for i in range(NUMBER_OF_RANDOM_NUMBERS_IN_LINE):
        quick_pick_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        while quick_pick_number in quick_pick_numbers:
            quick_pick_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        quick_pick_numbers.append(quick_pick_number)

def display_quick_pick_numbers(quick_pick_numbers):
    quick_pick_numbers.sort()
    for quick_pick_number in quick_pick_numbers:
        print(f"{quick_pick_number:2}", end=" ")
    print(sep="")
    # print(f"{" ".join(sorted(str(quick_pick_number) for quick_pick_number in quick_pick_numbers)):2}")

main()