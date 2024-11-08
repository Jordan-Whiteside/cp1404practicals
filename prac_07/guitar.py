"""
Class guitar.
Predicted: 5min
Actual: 5min
"""

VINTAGE_AGE = 2024
CURRENT_YEAR = 50


class Guitar:
    """Guitar class."""

    def __init__(self, name="", year=0, cost=0.0):
        """Construct guitar from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Get the age of a guitar based on the CURRENT YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is considered vintage based on age."""
        return Guitar.get_age(self) >= VINTAGE_AGE
