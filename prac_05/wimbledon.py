"""
CP1404 Practical
Wimbledon - program
Estimate: 20 mins
Actual: 37 mins
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read the wimbledon.csv file and prints information about the champions and countries."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def load_records(filename):
    """Return records from the wimbledon.csv file as list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create a dictionary of the champions and the no. of wins and set of countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display the champions with the corresponding no. of wins and the countries in alphabetical order."""
    print("Wimbledon Champions: ")
    max_length = max(len(name) for name in champion_to_count.keys())
    for name, count in champion_to_count.items():
        print(f"{name:{max_length}} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
