"""
Class programming languages
Predicted: 15min
Actual: 10min
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from given values."""
        self.name = name
        self.typing = typing.title()
        self.reflection = bool(reflection)
        self.year = int(year)

    def __str__(self):
        """Return string representation of a ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic."""
        return self.typing == "Dynamic"
