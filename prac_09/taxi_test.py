"""
CP1404 practical
Taxi test
"""

from prac_09.taxi import Taxi


def main():
    """test taxi"""
    my_taxi = Taxi("Prius 1", 100)
    print(my_taxi)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


main()