from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    km_output = StringProperty()

    def build(self):
        """Build app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.km_output = "Type distance in miles"
        return self.root

    def handle_increment(self, increment):
        """Handle and increment change of up or down."""
        miles = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(miles)

    def handle_calculate(self):
        """Handle Calculating miles displaying in a label widget."""
        miles = self.get_valid_miles()
        kilometers = miles * CONVERSION_MILES_TO_KM
        self.root.ids.output_label.text = str(kilometers)

    def get_valid_miles(self):
        """Get a valid mile using exception handling."""
        try:
            mile = float(self.root.ids.input_miles.text)
            return mile
        except ValueError:
            return 0.0


ConvertMilesKm().run()
