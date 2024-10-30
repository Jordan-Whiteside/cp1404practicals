"""
Class programming languages
Predicted: 15min
Actual: 10min
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year=0):
        self.name = name
        self.typing = typing.title()
        self.reflection = bool(reflection)
        self.year = int(year)

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
