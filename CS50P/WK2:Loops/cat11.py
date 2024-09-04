# Demonstrates defining functions

# Example 1
def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()


# Example 2
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))  
        if n > 0:
            break
    return n   

def meow(n):
    for _ in range(n):
        print("Meow!!!") 

main()

