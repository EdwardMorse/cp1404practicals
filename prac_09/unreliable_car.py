"""
CP1404 Practical
Unreliable Car class
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an unreliable car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the unreliable car a certain distance."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        return super().drive(distance)
