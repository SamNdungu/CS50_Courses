# Check __name__


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

# This block is commonly used to define code that should only run when the script is executed directly, and not when it is imported.
if __name__ == "__main__":
    main()
