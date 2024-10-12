"""Module 4 - Quick Picks"""

from random import randint

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 6
NUMBER_OF_RANDOM_NUMBERS_IN_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick_numbers = []
    for j in range(NUMBER_OF_RANDOM_NUMBERS_IN_LINE):
        quick_pick_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        while quick_pick_number in quick_pick_numbers:
            quick_pick_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        quick_pick_numbers.append(quick_pick_number)
    quick_pick_numbers.sort()
    print(quick_pick_numbers)
