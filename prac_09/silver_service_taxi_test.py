"""
CP1404 Practical
Silver service taxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver Service Taxi."""
    taxi = SilverServiceTaxi("Porsche", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
