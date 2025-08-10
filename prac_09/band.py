"""
CP1404 Practical
Band class
"""

class Band:
    """Band class."""
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def add(self, musician):
        """Add musician."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of the musicians playing."""
        return "\n".join(musician.play() for musician in self.musicians)

