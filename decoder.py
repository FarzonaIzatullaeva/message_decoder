import string
print("Hello, give the text: ")

entry = input()

print("Select the mode: (1 for encode 2 for decode): ")
decode_mode = input()

letters = string.ascii_lowercase

# print(letters)
new_word = ""


if (decode_mode == "1"):
    for e in entry:
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
    print(new_word + ": is the new encoded word for " + entry)

elif (decode_mode == "2"):
    for e in entry:
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
    print(new_word + ": is the new decoded word for " + entry)

else:
    print("error was made")
