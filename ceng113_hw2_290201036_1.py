# Checking Email
def checkUsername(username):
    ALPHANUMERIC_CHARACTEHRS = "abcdefghijklmnopqrstuvwxyz1234567890"
    global message
    global isAlphanumeric
    global notAlphanumericLetter

    isAlphanumeric = True

    # Is alphanumeric?
    for i in username:
        if (i.lower() in ALPHANUMERIC_CHARACTEHRS) == False:
            isAlphanumeric = False
            notAlphanumericLetter = i
            break

    if len(username) < 6:
        message = "-> Your username is not less than 6 characters length"
        return False

    elif len(username) > 12:
        message = "-> Your username is not greater than 12 characters length"
        return False

    elif username[0].lower() != "e":
        message = "-> Please use 'e' at the begining of the username"
        return False

    elif isAlphanumeric == False:
        message = f"-> Please use alphanumeric characters. Character '{notAlphanumericLetter}' is invalid."
        return False

    return True


# Checking Password
def checkPassword(password):
    if len(password) < 8:
        print("-> Password must be at least 8 characters\n")
        return False
    else:
        return True


def main():
    print("\n******************************\n")
    print("- User Registration Panel -\n")
    print("******************************")

    while True:
        username = input("\n// Please write your username: ")

        if checkUsername(username):
            break
        else:
            print(message)

    while True:
        password = input("// Please enter password: ")

        if checkPassword(password):
            print("\n- Registration Done! -")
            print("| username:", username)
            print("| password", password, "\n")
            break


if __name__ == "__main__":
    main()
