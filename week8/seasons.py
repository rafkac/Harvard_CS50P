from datetime import date
import re
import inflect


def main():
    d_of_birth = get_date(input("Date of Birth: "))
    print(minutes_str(d_of_birth))


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


def minutes_str(date):
    mins = int((date.today() - date).total_seconds() / 60)
    p = inflect.engine()
    words = p.number_to_words(mins)
    return f"{words} minutes"


if __name__ == "__main__":
    main()
