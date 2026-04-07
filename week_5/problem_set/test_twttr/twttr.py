def main():
    word = shorten(input("Input: "))
    print("Output:", word)


def shorten(word):
    result = ""
    for c in word:
        if c not in "aeiouAEIOU":
            result = result + c
    return result


if __name__ == "__main__":
    main()
