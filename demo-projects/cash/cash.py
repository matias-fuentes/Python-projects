from cs50 import get_float

def main():

    coins = 0
    owe = get_float("How much did I owe you?: ")
    while (owe <= 0.009):
        owe = get_float("How much did I owe you?: ")

    print("Change owed:", + owe)

    if (owe >= 0.25):

        repetition = int(owe / 0.25)

        while (coins < repetition):

            owe -= 0.25
            coins += 1

        if (owe >= 0.1):

            owe -= 0.1
            coins += 1

        if (owe >= 0.05):

            owe -= 0.05
            coins += 1

        if (owe >= 0.009):

            coins += 1

        print(coins)

    elif (owe >= 0.1):

        owe -= 0.1
        coins += 1

        if (owe >= 0.049):

            owe -= 0.05
            coins += 1

            if (owe >= 0.009):

                coins += 1

        print(coins)

    elif (owe >= 0.05):

        owe -= 0.05
        coins += 1

        if (owe >= 0.009):

            coins += 1

        print(coins)

    elif (owe <= 0.01):

        coins += 1
        print(coins)

main()