"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data"


def main():
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    subject = []
    input_file = open("subject_data")
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))

main()