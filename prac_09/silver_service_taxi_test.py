"""Test program for sliver service taxi class."""

from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 200, 2)

print(my_taxi.drive(18))
print(my_taxi.get_fare())
# assert my_taxi.drive(18)