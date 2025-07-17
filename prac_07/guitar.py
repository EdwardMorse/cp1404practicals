"""
CP1404 Practical - Guitar class file.
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Guitar class."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a Guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare guitars from oldest to newest."""
        return self.year < other.year