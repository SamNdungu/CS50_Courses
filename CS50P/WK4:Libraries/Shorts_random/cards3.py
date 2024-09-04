import random

cards = ["jack", "queen", "king"]


def main():

    # 'Jack' has a 100% chance to be chosen - user will always choose 'Jack'
    print(random.choices(cards, weights=[100, 0, 0], k=2))

    # 'Jack', 'queen', and 'king' has 65%, 20%, and 15% chance to be chosen respectively
    print(random.choices(cards, weights=[65, 20, 15], k=2))

    # 'random.seed(x)' makes the sure you get the same results
    random.seed(1)
    print(random.choices(cards, weights=[65, 20, 15], k=2))

main()
