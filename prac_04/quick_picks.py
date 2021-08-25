"""
CP1404/CP5632 Practical
Quick picks random lottery numbers
"""
import random

AMOUNT_OF_RANDOM_NUMBERS = 6
LOWER_RANDOM_VALUE = 1
UPPER_RANDOM_VALUE = 45

quick_picks = []
for i in range(AMOUNT_OF_RANDOM_NUMBERS):
    random_number = random.randint(LOWER_RANDOM_VALUE, UPPER_RANDOM_VALUE)
    while random_number in quick_picks:
        random_number = random.randint(LOWER_RANDOM_VALUE, UPPER_RANDOM_VALUE)
    quick_picks.append(random_number)
quick_picks.sort()
print(quick_picks)
