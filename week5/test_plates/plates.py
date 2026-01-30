def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters_first = s[0:2].isalpha()
    correct_length = True if 2 <= len(s) <= 6 else False
    specials = [' ', '.', ',']
    no_specials = all(special not in s for special in specials)

    # Numbers cannot be used in the middle of a plate;
    # they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
    # AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.

    digit_started = False
    for c in s:
        if (c.isdigit()) and not digit_started and c == "0":
            return False
        elif c.isdigit() and not digit_started:
            digit_started = True
        elif digit_started and c.isalpha():
            return False

    return letters_first and correct_length and no_specials


if __name__ == "__main__":
    main()
