def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)

    match y:
        case "+":
            print(round((x+z), 1))
        case "-":
            print(round((x-z), 1))
        case "*":
            print(round((x*z), 1))
        case _: #assume valid operators
            print(round((x/z), 1))

main()
