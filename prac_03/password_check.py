"""Check password length"""

PASSWORD_MINIMUM_LENGTH = 10

password = input("Enter your password: ")
while len(password) < PASSWORD_MINIMUM_LENGTH:
    print(f"Your password has to be longer than {PASSWORD_MINIMUM_LENGTH} characters")
    password = input("Enter your password: ")
for character in password:
    print("*", end="")
