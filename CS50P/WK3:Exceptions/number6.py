# Removes break
# Define a function main()
def main():
    x = get_int()
    print(f"x is {x}")


# Define a function get_int()
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            # `return x` is better than `break`. it will not only break you out of the loop but it will also return a value.
            return x


main()
