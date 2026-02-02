import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # unique video ID at the end of url consist of 11 alphanumeric characters, hyphens, and underscores
    pattern = r'<iframe.+"https?://(?:www\.)?youtube\.com/embed/([\w-]{11})"'
    match = re.search(pattern, s)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
