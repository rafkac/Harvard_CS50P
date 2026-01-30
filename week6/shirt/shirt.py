import sys
import os


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python input_file output_file")

    ext1 = os.path.splitext(filename1)[1]
    ext2 = os.path.splitext(filename2)[1]

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")







if __name__ == "__main__":
    main()
