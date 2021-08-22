"""
CP1404/CP5632 - Practical
Learning about generating random numbers
"""

import random

# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# Smallest is 5, largest is 20
#
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# Smallest is 3, largest is 9, but the code only produce odd numbers, so it cannot produced a 4
#
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Smallest is 2.5, largest is 5.5, but the returned number is a float type

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
