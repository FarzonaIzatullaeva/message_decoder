import string

letters = string.ascii_lowercase

# Author: Farzonakhon Izatullaeva


def decoder(word, command):
    new_word = ""

    if (command == "1"):
        for e in word:
            isUpper = e.isupper()
            if (e.lower() in letters):
                letter = letters.find(e.lower())

                new_index = (letter+3) % 26

                new_letter = letters[new_index]

                if (isUpper):
                    new_word += new_letter.upper()
                else:
                    new_word += new_letter

            else:
                new_word += e
        return (new_word)

    elif (command == "2"):
        for e in word:
            isUpper = e.isupper()
            if (e.lower() in letters):
                letter = letters.find(e.lower())

                new_index = (letter-3) % 26

                new_letter = letters[new_index]

                if (isUpper):
                    new_word += new_letter.upper()
                else:
                    new_word += new_letter

            else:
                new_word += e
        return (new_word)

    else:
        return ("Error was made.")


def main():
    print("Hello, give the text: ")

    entry = input()

    print("Select the mode: (1 for encode 2 for decode): ")
    decode_mode = input()

    print(decoder(entry, decode_mode))


if __name__ == "__main__":
    main()
