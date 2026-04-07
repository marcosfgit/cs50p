def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Verify if first two characters are letters
    for c in s[0:2]:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False

    # Verify if plate has 2-6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Verify if first number is not a zero
    for c in range(len(s)):
        if s[c].isdigit():
            if s[c] == "0":
                return False
            break

    # Verify if there are letters after any number
    for c in range(len(s)):
        if s[c].isdigit():
            if not s[c:].isdigit():
                return False
            break

    # Verify if there is any periods, spaces or punctuations
    for c in s:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            return False

    # If it passed through all the checks:
    return True


if __name__ == "__main__":
    main()
