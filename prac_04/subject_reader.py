"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_record(data)


def display_subject_record(subject_records):
    """Display the details of a subject"""
    for subject_record in range(len(subject_records)):
        # list formated like [[subject, lecturer, number of students], [subject, lecturer, number of students]]
        print(f"{subject_records[subject_record][0]} is taught by {subject_records[subject_record][1]} and has {subject_records[subject_record][2]} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []
    input_file = open(FILENAME)
    for i, line in enumerate(input_file):
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subject_records.append(parts)
        print("----------")
    input_file.close()
    return subject_records


main()

# display_subject_detail([['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]])
