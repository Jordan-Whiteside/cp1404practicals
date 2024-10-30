"""Class guitar."""

class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return 2024 - self.year

    def is_vintage(self):
        return Guitar.get_age(self) >= 50

