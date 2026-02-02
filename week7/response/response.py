from validator_collection import validators, errors


def main():
    email_addy = input("What's your email address? ")

    try:
        validators.email(email_addy)
        print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")


if __name__ == "__main__":
    main()
