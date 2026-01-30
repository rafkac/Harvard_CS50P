from pyfiglet import Figlet
import sys
from random import choice


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # 0 arguments -> choose font at random
    if len(sys.argv) == 1:
        font = choice(fonts)
    # 2 arguments -> get font from last argumentl
    elif len(sys.argv) == 3:
        # check for valid first argument
        if (sys.argv[1] not in ["-f", "--font"]):
            sys.exit("invalid first argument\ncorrect usage: python figlet.py -f font_name")
        elif (sys.argv[2] not in fonts):
            sys.exit("invalid font\ncorrect usage: python figlet.py -f font_name")
        else:
            font = sys.argv[2]
    # must provide 0 or 2 arguments:
    else:
        sys.exit("invalid program call\ncorrect usage: python figlet.py -f font_name")

    figlet.setFont(font=font)
    text = input("Input: ")
    print("Output: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
