# Demonstrates defining a function with a return value

def main():
    x = int(input("What's x?: "))
    print("X squared is", square(x))  


def square(n):
    return n * n     

if __name__ == "__main__":
    main()
