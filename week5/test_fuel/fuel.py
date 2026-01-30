def main():
    while True:
        try:
            division = input("Fraction: ")
            fraction = convert(division)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    print(gauge(fraction))


def convert(fraction):
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("x cannot be greater than y")
    if x/y < 0:
        raise ValueError("fraction cannot be negative")

    return round(x / y * 100)


def gauge(percentage):
    match percentage:
        case x if x >= 99:
            return "F"
        case x if 1 < x < 99:
            return f"{percentage}%"
        case _:
            return "E"


if __name__ == "__main__":
    main()
