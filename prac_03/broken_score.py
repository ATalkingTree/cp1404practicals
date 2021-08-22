"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)
    random_score = random.randint(0, 100)
    result = determine_score_status(random_score)
    print(f"Random score is {random_score} and this is {result.lower()}")


def determine_score_status(score):
    if 0 > score or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()
