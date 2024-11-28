"""Test program for sliver service taxi class."""

from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 200, 2)

assert my_taxi.drive(18) == 18
print(my_taxi.get_fare())
assert my_taxi.get_fare() == 48.8
# assert my_taxi.drive(18)
