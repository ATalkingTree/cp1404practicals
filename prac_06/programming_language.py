"""CP1404/CP5632 Practical - Programming Language class."""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a Car instance.

        name: string, name of the programming language
        typing: string, either "Dynamic" or "Static"
        reflection: boolean, to determine if a language supports reflection or not
        year: integer, released year of the language
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
