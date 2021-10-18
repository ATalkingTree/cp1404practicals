"""CP1404/CP5632 Practical - Guitar class."""

VINTAGE_AGE = 50
CURRENT_YEAR = 2021

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Car instance.

        name: string, name of the guitar
        year: integer, the year it is made in
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        return self.get_age() > 50
