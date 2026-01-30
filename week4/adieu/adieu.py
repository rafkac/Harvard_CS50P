import inflect


def main():
    p = inflect.engine()
    names = []

    try:
        while True:
            names.append(input("Name: ").strip())
    except EOFError:
        print()

    adieu = p.join(names)
    print(f"Adieu, adieu, to {adieu}")


main()
