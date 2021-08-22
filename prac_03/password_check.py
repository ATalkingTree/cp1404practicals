"""Check password length"""

PASSWORD_MINIMUM_LENGTH = 10


def main():
    """Check password length"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    for character in password:
        print("*", end="")


def get_password():
    password = input("Enter your password: ")
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        print(f"Your password has to be longer than {PASSWORD_MINIMUM_LENGTH} characters")
        password = input("Enter your password: ")
    return password


main()
