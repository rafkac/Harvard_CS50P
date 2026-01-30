def main():
    name = input("Input: ")
    print("Output:", shorten(name))


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    for c in word:
        if not c.lower() in vowels:
            result += c
            
    return result

if __name__ == "__main__":
    main()
