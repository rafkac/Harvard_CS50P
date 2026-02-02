import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    Convert a working hours string to duration in hours.

    Accepted formats:
    - "9:00 AM to 5:00 PM"
    - "9 AM to 5 PM"
    - "9:00 AM to 5 PM"
    - "9 AM to 5:00 PM"

    Raises ValueError if format is invalid or times are out of range.
    Returns the duration in hours.
    """
    pattern = r"(\d{1,2})(?::00)?\s*([AP]M)\s+to\s+(\d{1,2})(?::00)?\s*([AP]M)"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError("Invalid time format")

    start_hour, start_am_pm, end_hour, end_am_pm = matches.groups()
    start_hour = int(start_hour)
    end_hour = int(end_hour)

    # validate hours are in valid range (1-12 for 12-hour format)
    if not is_hour_valid(start_hour):
        raise ValueError("Invalid start hour")
    if not is_hour_valid(end_hour):
        raise ValueError("Invalid end hour")

    # convert to 24-hour format
    start_hour = to_24_hour(start_hour, start_am_pm)
    end_hour = to_24_hour(end_hour, end_am_pm)

    # handle case where end time is on the next day
    if end_hour < start_hour:
        end_hour += 24

    return end_hour - start_hour


def is_hour_valid(h):
    return 1 <= start_hour <= 12


def to_24_hour(hour, period):
    """Convert hour and AM/PM period to 24-hour format."""
    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12


if __name__ == "__main__":
    main()
