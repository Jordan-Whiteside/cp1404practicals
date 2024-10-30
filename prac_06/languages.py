"""
Languages program
Predicted: 10min
Actual: 10min - about 1 hour if I include finding out I can just do .name for its name *facepalm*
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
# print(python)

