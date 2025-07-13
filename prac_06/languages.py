"""
CP1404 Practical - languages client file.
Estimated time - 20 mins
Actual time - 30 mins
"""

from programming_language import ProgrammingLanguage


def main():
    """Determine if a programming language is dynamically typed."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, visual_basic]
    print(python)
    print(ruby)
    print(visual_basic)
    print("The dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
