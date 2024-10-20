"""
Wimbledon
Estimated: 1 hour
Actual: 2 hours 7 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Get a record of Wimbledon champions, process that into a dictionary and set then display them"""
    records = get_records_from_file(FILENAME)
    champion_to_win, country_codes = get_champion_wins_and_countries(records)
    display_wimbledon_champions_and_countries(champion_to_win, country_codes)


def display_wimbledon_champions_and_countries(champion_to_win, country_code):
    """Display wimbledon champions and there wins as well as what countries have won"""
    print("Wimbledon Champions")
    for champion, win in champion_to_win.items():
        print(f"{champion} {win}")
    print(sep="")
    print(f"These {len(country_code)} countries have won Wimbledon:")
    print(", ".join(sorted(country_code)))


def get_champion_wins_and_countries(records):
    """Create a dictionary with champion name paired with win(s) and countries code into a set"""
    champion_to_win = {}
    # record contains Year, Country, Champion, Country, Runner-up, Score in the final
    for record in records:
        champion_to_win[record[2]] = champion_to_win.get(record[2], 0) + 1
    country_code = {record[1] for record in records}
    return champion_to_win, country_code


def get_records_from_file(filename):
    """Get records from a file returning a list of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # record fields Year, Country, Champion, Country, Runner-up, Score in the final
        number_of_fields = in_file.readline().count(',')
        records = [line.strip().split(',', number_of_fields) for line in in_file]
    return records


main()
