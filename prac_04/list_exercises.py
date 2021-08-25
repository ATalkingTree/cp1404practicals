"""
CP1404/CP5632 Practical
Intermediate exercises
"""


def main():
    basic_list_operations()


def basic_list_operations():
    NUMBER_OF_NUMBERS = 5
    number_lists = []
    for i in range(NUMBER_OF_NUMBERS):
        user_input = int(input("Number: "))
        number_lists.append(user_input)
    print(f"The first number is {number_lists[0]}")
    print(f"The last number is {number_lists[-1]}")
    print(f"The smallest number is {min(number_lists)}")
    print(f"The largest number is {max(number_lists)}")
    print(f"The average of the numbers is {sum(number_lists) / len(number_lists)}")


main()
