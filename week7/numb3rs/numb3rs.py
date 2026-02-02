import re


def main():
    print(validate(input("IPv4 Address: ")))


# x.x.x.x where x is 0-255
def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    numbers = re.search(pattern, ip)

    if numbers:
        return all(isByte(n) for n in numbers.groups())
    return False


# check whether string is numerical 0-255 inclusive
def isByte(d):
    try:
        # invalidate cases like 01 or 001
        return 0 <= int(d) <= 255 and not (d.startswith('0') and len(d) > 1)
    except ValueError:
        return False


if __name__ == "__main__":
    main()
