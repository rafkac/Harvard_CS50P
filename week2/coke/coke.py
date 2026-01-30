def main():
    due = 50
    valid_coins = [25, 10, 5]
    print("Amount Due: ", due)

    while due > 0:
        coin = int(input("Insert Coin: "))
        if coin in valid_coins:
            due -= coin

        print("Amount Due:", due)

    print("Change Owed:", -due)

main()
