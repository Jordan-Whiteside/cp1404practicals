"""Test Taxi program."""

from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
print(my_taxi.drive(40))
print(my_taxi, f"Current fare ${my_taxi.get_fare()}")
my_taxi.start_fare()
print(my_taxi.drive(100))
print(my_taxi, f"Current fare ${my_taxi.get_fare()}")