# Adds functions, uses break and return


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            # You can put `break` here and avoid else block
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
