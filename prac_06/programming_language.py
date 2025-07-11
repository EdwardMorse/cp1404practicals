"""
CP1404 Practical - programming language class file.
Estimated time - 20 mins
Actual time - 30 mins
"""


class ProgrammingLanguage:
    """Programming language class."""

    def __init__(self, name, typing, reflection, year):
        """Initialise Programming Language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a program is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a Programming Language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"