import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv")

    # get files from argvs
    before = sys.argv[1]
    after = sys.argv[2]

    # list of dictionaries to be appended
    students = []

    try:
        with open(before) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                students.append({
                    "first": first,
                    "last": last,
                    "house": house
                })
    except FileNotFoundError:
        sys.exit("File does not exist.")

    with open(after, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for s in students:
            writer.writerow(s)


if __name__ == "__main__":
    main()
