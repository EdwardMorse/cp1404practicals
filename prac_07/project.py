"""
CP1404 Practical 7 project class program.
"""


class ProjectManagement:
    """Project management class."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialises a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Returns a string representation of the project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage:.2f}%"

    def __lt__(self, other):
        """Compare projects based on priority."""
        return self.priority < other.priority

    def is_completed(self):
        """Determines if a project is completed."""
        return self.completion_percentage == 100
