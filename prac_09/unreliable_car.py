"""Unreliable car class."""
from random import uniform

from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of Car class that has reliability issues."""

    def __init__(self, name, fuel, reliability):
        """Constructor for an Unreliable Car object"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = uniform(0,100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven