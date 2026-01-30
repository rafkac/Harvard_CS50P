import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a csv file")

    lines = []

    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)

    print(tabulate(lines, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
