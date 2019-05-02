"""
CP1404
converts miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_PER_KILOMETRES = 1.609

class MilesToKilometers(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Miles to kilometres Converter"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def convert_miles_to_kilometers(self):
        value = self.validate_input()
        result = value * MILES_PER_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        miles = self.validate_input() + increment
        self.root.ids.input_number.text = str(miles)
        self.convert_miles_to_kilometers()

    def validate_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometers().run()
