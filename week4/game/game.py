from random import randint
import sys


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            continue

    n = randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            elif guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            continue


main()
