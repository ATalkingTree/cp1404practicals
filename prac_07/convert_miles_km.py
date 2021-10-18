"""
Miles to Kilometres Converter
CP1404 Practical
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometersApp(App):
    """ MilesToKilometersApp is a Kivy App for converting miles to km """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesToKilometersApp().run()
