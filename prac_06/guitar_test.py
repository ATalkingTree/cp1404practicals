"""CP1404/CP5632 Practical - Client code to use the Guitar class."""


from prac_06.guitar import Guitar


CURRENT_YEAR = 2021

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

gibson = Guitar(name, year, cost)
another_guitar = Guitar("Another Guitar", 2013)

print("{} get_age() - Expected 99. Got {}".format(gibson.name, gibson.get_age()))
print("{} get_age() - Expected 8. Got {}".format(another_guitar.name, another_guitar.get_age()))

print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))
