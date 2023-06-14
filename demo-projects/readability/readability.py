from cs50 import get_string

def main():

    letterCounter = 0.0
    wordCounter = 1.0
    sentenceCounter = 0.0
    i = 0

    text = get_string("Put your text to evaluate its grade level: ")

    while (i < len(text)):

        if (text[i] == " "):

            wordCounter += 1

        elif (text[i] == "." or text[i] == "!" or text[i] == "?"):

            sentenceCounter += 1

        elif (text[i] != "," and text[i] != "\"" and text[i] != ":" and text[i] != ";"):

            letterCounter += 1

        i += 1

    L = letterCounter / wordCounter * 100
    S = sentenceCounter / wordCounter * 100
    floatIndex = 0.0588 * L - 0.296 * S - 15.8

    if (floatIndex < 0):

        print("Before Grade 1")

    elif (floatIndex >= 1 and floatIndex < 16):

        floatIndex = round(floatIndex)
        print(f"Grade {floatIndex}")

    else:

        print("Grade 16+")

main()