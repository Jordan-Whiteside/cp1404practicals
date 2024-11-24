"""Unreliable car test."""

from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("Shit box", 1000, 50)
for i in range(100):
    print(my_unreliable_car.drive(10))
