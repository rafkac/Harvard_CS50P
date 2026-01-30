def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        try:
            date = input("Date: ").strip()

            # eg. September 8, 1636
            if "," in date:
                month_day, year_str = date.split(",")
                month_str, day_str = month_day.split()
                month = months[month_str.capitalize()]

            # eg. 8/9/1636
            elif "/" in date:
                month_str, day_str, year_str = date.split("/")
                month, day, year = map(int, [month_str, day_str, year_str])

            else:
                raise ValueError

            day, month, year = int(day_str), int(month), int(year_str)

            if not (1 <= day <= 31 and 1 <= month <= 12):
                raise ValueError

            print(f"{year}-{month:02}-{day:02}")
            break

        except (ValueError, KeyError):
            continue


main()
