"""Module 4 - Quick Picks"""

from random import randint

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick_numbers = []
    for j in range(number_of_quick_picks):
        quick_pick_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        quick_pick_numbers.append(quick_pick_number)
    print(quick_pick_numbers)
