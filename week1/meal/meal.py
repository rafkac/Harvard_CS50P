def main():
    time = input("What time is it? ")
    actualTime = convert(time)

    if 7 <= actualTime <= 8:
        print("breakfast time")
    elif 12 <= actualTime <= 13:
        print("lunch time")
    elif 18 <= actualTime <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
