import sys
from datetime import date
import re
import inflect


def main():
    try:
        d_of_birth = get_date(input("Date of Birth: "))
        print(minutes_str(d_of_birth))
    except ValueError:
        sys.exit("Invalid date")


# must be YYYY-MM-DD
def get_date(d):
    pattern = r"^(\d{4})-(\d{2})-(\d{2})$"
    matches = re.search(pattern, d)
    if not matches:
        raise ValueError("Invalid date")

    year, month, day = map(int, matches.groups())

    try:
        date_obj = date(year, month, day)
        return date_obj
    except ValueError:
        raise ValueError("Invalid date")


def minutes_str(d):
    mins = int((date.today() - d).total_seconds() / 60)
    p = inflect.engine()
    words = p.number_to_words(mins).capitalize()
    words = words.replace(" and ", " ") # remove 'and' to pass the check50 tests

    return f"{words} minutes"


if __name__ == "__main__":
    main()
