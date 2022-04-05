from cs50 import get_int

def main():

    pyramidSize = get_int("Size of the pyramid? Please, input a number between one and eight: ")

    while (pyramidSize < 1 or pyramidSize > 8):

        pyramidSize = get_int("Size of the pyramid? Please, input a number between one and eight: ")

    i = pyramidSize

    while (i > 0):

        j = 0

        while (j < pyramidSize):

            if i <= j + 1:
                print("#", end="")
            else:
                print(" ", end="")

            j += 1

        print()
        i -= 1

main()