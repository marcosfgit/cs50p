s = input("Input: ")

print("Output: ", end="")

for c in s:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        print("", end="")
    else:
        print(c, end="")

print()
