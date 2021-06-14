import random


def flip_coin():
    count = 0
    heads_count = 0
    tails_count = 0
    flips_count = int(input("How many flips?: "))

    for flip in range(flips_count):
        result = random.randint(0, 1)
        count += 1
        if result == 0:
            result = "Heads"
            heads_count += 1
        else:
            result = "Tails"
            tails_count += 1
        print(f"{count}: {result}")
    print(f"\nSummary:\n    Heads: {heads_count}\n    Tails: {tails_count}")


flip_coin()
