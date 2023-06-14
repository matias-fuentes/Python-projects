import sys
import csv

def main():

    if (len(sys.argv) != 3):

        sys.exit("Usage: python dna.py data.csv sequence.txt")

    strs = []
    check = []
    repeats = []
    maxRepeats = []

    with open(f"{sys.argv[1]}") as database:
        reader = csv.reader(database)

        for row in reader:

            i = 1

            while (i < len(row)):

                strs.append(row[i])
                strs.append(0)
                i += 1

            break

        for row in reader:

            i = 0

            while i < len(row):

                if (i == 0):

                    check.append(row[i])
                    i += 1

                else:

                    check.append(int(row[i]))
                    i += 1

    with open(f"{sys.argv[2]}") as sequence:
        for line in sequence:
            stringSequence = line
            break

    n = -1
    for i in range(0, len(strs), 2):

        j = 0
        l = 0
        k = len(strs[i])

        while (k < len(stringSequence)):

            if (stringSequence[j:k] != strs[i]):

                j += 1
                k += 1

            else:

                if (j == l + len(strs[i])):

                    repeats[n] += 1

                else:

                    repeats.append(1)
                    n += 1

                l = j
                m = k
                j += 1
                k += 1
        repeats.append(0)
        n += 1

    i = 0
    tmp = 0

    while (i < len(repeats) - 1):

        while (repeats[i] != 0):

            tmp = max(repeats[i], tmp)
            i += 1

        i += 1
        maxRepeats.append(tmp)
        tmp = 0

    i = 1
    j = 0
    test = False

    while (i < len(check)):

        if (check[i] == maxRepeats[j]):

            if (j == len(maxRepeats) - 1):

                print(check[i - j - 1])
                test = True
                break

            j += 1

        else:

            j = 0

        i += 1

    if (test == False):

        print("No match")

main()