"""
CP1404/CP5632 - Practical
Practice reading / writing files
"""

# Question 1
output_file = open("name.txt", "w")
user_name = input("Enter your name: ")
output_file.write(user_name)
output_file.close()

# Question 2
input_file = open("name.txt", "r")
user_name = input_file.read()
print(f"Your name is {user_name}")
input_file.close()

# Question 3
input_file = open("numbers.txt", "r")
first_number = int(input_file.readline())
second_number = int(input_file.readline())
total = first_number + second_number
print(total)
input_file.close()

# Question 4
input_file = open("numbers.txt", "r")
total = 0
for line in input_file:
    total += int(line)
print(total)
input_file.close()
