"""
Miles to Kilometres Converter
CP1404 Practical
"""

from kivy.app import App
from kivy.app import StringProperty
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKilometersApp(App):
    """ MilesToKilometersApp is a Kivy App for converting miles to km """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, number, increment):
        """ increase the number in input field by the increment amount """
        number = self.get_valid_number(number)
        result = float(number) + increment
        self.root.ids.input_number.text = str(result)

    def convert(self, number):
        """ handle calculation (could be button press or other call), output result to label widget """
        number = self.get_valid_number(number)
        result = float(number) * MILES_TO_KM
        self.message = str(result)

    def get_valid_number(self, number):
        """ get text input from text entry widget, convert to float
            return 0 if error, float version of text if valid"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometersApp().run()
