def charCounter(text, character):
    counter = 0
    for char in text:
        if char.upper() == character.upper():
            counter += 1

    return counter


def main():
    text = input("\n// Write your text: \n")
    special_char = input("\n// Please enter a character: ")

    charCount = charCounter(text, special_char)
    print(
        f"\n| We have found '{charCount}' special character '{special_char}' |")


if __name__ == "__main__":
    main()
