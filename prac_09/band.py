"""Band class."""


class Band:
    """Representation of a band object."""

    def __init__(self, name):
        """Initialise an instance of a band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Display a string representation of a band."""
        return f"{self.name} ({", ".join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Play instrument for each band member."""
        for musician in self.musicians:
            print(musician.play())
