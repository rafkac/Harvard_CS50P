def main():
    while True:
        try:
            division = input("Fraction: ")
            x_str, y_str = division.split("/")
            x = int(x_str)
            y = int(y_str)
            if x > y:
                raise ValueError("x cannot be greater than y")
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    match (x/y):
        case x if x >= 0.99:
            print("F")
        case x if 0.01 < x < 0.99:
            print(float_to_percentage(x))
        case _:
            print("E")


def float_to_percentage(x):
    return f"{round(x*100)}%"


main()
