"""
CP1404 Practical 8
Miles to kilometers conversion program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

KILOMETERS_PER_MILE_CONVERSION = 1.60934


class MilesToKilometers(App):
    """Convert miles to kilometers."""
    output = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (800, 600)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculation(self):
        """Handles calculation and outputs result to label widget."""
        value = self.get_valid_miles()
        result = value * KILOMETERS_PER_MILE_CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value_change):
        """Handle increment of input number with up/down buttons."""
        value = self.get_valid_miles() + value_change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def get_valid_miles(self):
        """Convert text to float or return 0.0 if invalid miles."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesToKilometers().run()
