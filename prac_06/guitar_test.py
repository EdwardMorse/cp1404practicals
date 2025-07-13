"""
CP1404 Practical - Guitar test file.
Estimated time - 20 mins
Actual time -  35 mins. Didn't realise I had inti instead of init.
"""

from guitar import Guitar


def run_tests():
    """Tests the Guitar class"""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1200.00)

    print(f"{guitar.name} get_age() - Expected {103}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {12}. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


if __name__ == "__main__":
    run_tests()
