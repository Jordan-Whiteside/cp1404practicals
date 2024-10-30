"""Class programming languages"""


class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year=0):
        self.language = language
        self.typing = typing.title()
        self.reflection = bool(reflection)
        self.year = int(year)

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
