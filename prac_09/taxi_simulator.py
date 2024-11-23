"""Taxi simulator program."""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            print("choose taxi")
        elif choice == "d":
            print("drive")
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>>").lower()

