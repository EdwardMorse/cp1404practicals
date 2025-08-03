"""
CP1404 Practical
Silver service taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents a silver service taxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize a silver service taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Returns a string representation of the silver service taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()
