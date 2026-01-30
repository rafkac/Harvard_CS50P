def main():
    answer = input("What is the Answer to the Great Quesiton of Life, the Universe, and Everything? ")
    match cleanStr(answer):
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


def cleanStr(s):
    return s.lower().strip()


main()
