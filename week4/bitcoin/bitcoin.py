import sys
import requests


def main():
    API_KEY = "c71c6a26efb805695057968fec74b05f58629f290faeeb600ad0b043970fc464"

    if len(sys.argv) != 2:
        sys.exit("Correct usage: python bitcoin.py bitcoin_ammount")

    # get float number of bitcoins
    try:
        bitcoin_ammount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + API_KEY)
    except requests.RequestException as e:
        print(f"API request failed: {e}")

    # store response in json object
    o = response.json()

    # price nicely formatted
    price = bitcoin_ammount * float(o["data"]["priceUsd"])
    print(f"${price:,.4f}")


if __name__ == "__main__":
    main()
