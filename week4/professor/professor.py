import random


def main():
    # prompt user for level (1-3)
    level = get_level()

    # generate 10 math problems
    problems = []
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problems.append((x, y))

    # prompts user to solve 10 problems
    score = 0
    for p in problems:
        solved = False
        correct = p[0] + p[1]
        # 3 tries
        for i in range(3):
            answer = int(input(f"{p[0]} + {p[1]} = "))
            if answer == correct:
                solved = True
                score += 1
                break
            else:
                print("EEE")
        # show solution
        if not solved:
            print(f"{p[0]} + {p[1]} = {p[0]+p[1]}")

    # print final score
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            continue


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case _:
            return random.randint(pow(10, level-1), pow(10, level) - 1)


if __name__ == "__main__":
    main()
