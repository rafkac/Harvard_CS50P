def main():
    grocery = {}

    try:
        while True:
            item = input().strip().upper()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
    except EOFError:
        print()
        pass

    for i in sorted(grocery):
        print(f"{grocery[i]} {i}")



main()
