"""Silver Service Taxi Class"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi class."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Constructor for a Silver Service Taxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Display a string representation of a SilverServiceTaxi object."""
        return f"{super().__str__()} plus {self.flagfall}"

    def get_fare(self):
        """Get the taxi fare."""
        return super().get_fare() + self.flagfall
