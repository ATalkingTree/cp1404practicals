"""
CP1404/CP5632 Practical
Storing emails and names
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    part = email.split("@")
    email_name = part[0].split(".")
    name = " ".join(email_name).title()
    return name


main()
