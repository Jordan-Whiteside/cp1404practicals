"""Taxi simulator program."""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Display menu for taxi simulator program."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0.00
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = get_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                drive_taxi(current_taxi)
                total_fare += current_taxi.get_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: {total_fare:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i}, {taxi}")


def get_taxi(taxis, current_taxi):
    """Get a taxi."""
    display_taxis(taxis)
    try:
        taxi_index = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_index]
    except ValueError:
        print("Invalid taxi choice")
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


def drive_taxi(current_taxi):
    """Drive taxi a distance that is not negative."""
    current_taxi.start_fare()
    try:
        travel_distance = int(input("Drive how far? "))
        if travel_distance < 0:
            print("Distance must be greater than 0")
            return
        current_taxi.drive(travel_distance)
    except ValueError:
        print("Invalid distance")
    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")


main()
