def main():
    name = input("camelCase: ")
    result = ""

    for c in name:
        if c.isupper():
            result = result + "_" + c.lower()
        else:
            result += c
    print("snake_case: ", result)


main()
