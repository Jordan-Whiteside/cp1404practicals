"""
Wimbledon
Estimated: 1 hour
Actual:
"""

from operator import itemgetter

FILENAME = "wimbledon.csv"


def main():
    records = get_records_from_file(FILENAME)
    print(records)


def create_champion_wins(records):
    """Create a dictionary with champion name paired with win(s)"""
    champion_to_win = {}
    for record in records:
        champion_to_win[record[2]] = champion_to_win.get(record[2], 0) + 1
    return champion_to_win


def get_records_from_file(filename):
    """Get records from a file returning a list of lists"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # record fields Year, Country, Champion, Country, Runner-up, Score in the final
        number_of_fields = in_file.readline().count(',')
        records = [line.strip().split(',', number_of_fields) for line in in_file]
    return records


main()
