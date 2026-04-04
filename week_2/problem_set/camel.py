s = input("camelCase: ")

for c in s:
    if c == c.upper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")

print()
