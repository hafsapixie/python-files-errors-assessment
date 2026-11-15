"""Student Attendance Cleaner.

Reads raw student names from attendance.txt, cleans them with strip() and
title(), removes duplicates with a set, sorts the names alphabetically, and
saves the result to attendance_clean.csv.
"""

import csv

INPUT_FILE = "attendance.txt"
OUTPUT_FILE = "attendance_clean.csv"
OUTPUT_FIELDNAME = "student_name"


def read_names(path: str) -> list[str] | None:
    """Read all lines from a text file.

    Returns None when the file is missing so main() can report the problem and
    stop without showing a traceback.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {path} was not found.")
        print("Place attendance.txt next to attendance_cleaner.py and try again.")
        return None


def clean_names(raw_names: list[str]) -> tuple[list[str], list[str]]:
    """Clean, de-duplicate, and sort student names.

    The list comprehension applies strip() and title() to every non-empty line.
    A set removes duplicate names, and sorted() returns an alphabetical list.
    """
    cleaned_names = [name.strip().title() for name in raw_names if name.strip()]
    unique_students = set(cleaned_names)
    sorted_students = sorted(unique_students)
    return cleaned_names, sorted_students


def save_clean_list(students: list[str]) -> None:
    """Write the cleaned and sorted names to attendance_clean.csv."""
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([OUTPUT_FIELDNAME])
        for student in students:
            writer.writerow([student])


def display_results(
    original_count: int, unique_count: int, sorted_students: list[str]
) -> None:
    """Print record counts and the cleaned attendance list."""
    print(f"Original records: {original_count}")
    print(f"Unique students: {unique_count}")
    print(f"Duplicates removed: {original_count - unique_count}")
    print("\nCleaned attendance list (sorted):")
    for index, student in enumerate(sorted_students, start=1):
        print(f"  {index}. {student}")
    print(f"\nSaved cleaned list to {OUTPUT_FILE}.")


def main() -> None:
    """Run the attendance cleaning process."""
    print("Student Attendance Cleaner")

    raw_names = read_names(INPUT_FILE)
    if raw_names is None:
        return

    cleaned_names, sorted_students = clean_names(raw_names)

    if not cleaned_names:
        print("No student records found in the file.")
        return

    save_clean_list(sorted_students)
    display_results(len(cleaned_names), len(sorted_students), sorted_students)


if __name__ == "__main__":
    main()