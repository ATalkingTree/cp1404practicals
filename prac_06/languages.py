"""CP1404/CP5632 Practical - Client code to use the Programming Language class."""


from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(ruby, python, visual_basic, sep='\n')
print()
languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
