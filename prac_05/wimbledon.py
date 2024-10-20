"""
Wimbledon
Estimated: 1 hour
Actual: 2 hours 7 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Get a record of Wimbledon champions, process that into a dictionary and set then display them."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def display_results(champion_to_win, countries):
    """Display wimbledon champions countries."""
    print("Wimbledon Champions")
    for champion, count in champion_to_win.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def process_records(records):
    """Create a dictionary of champion name paired with win(s) and set of countries from records."""
    champion_to_win = {}
    countries = set()
    # record contains Year, Country, Champion, Country, Runner-up, Score in the final
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        champion_to_win[record[INDEX_CHAMPION]] = champion_to_win.get(record[INDEX_CHAMPION], 0) + 1
    return champion_to_win, countries


def get_records(filename):
    """Get records from a file returning a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        records = []
        # record fields Year, Country, Champion, Country, Runner-up, Score in the final
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records


main()
