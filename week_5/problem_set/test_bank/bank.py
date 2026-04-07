def main():
    output = value(input("Greeting: "))
    print("$", output, sep="")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting[:5] == "hello":
        amount = 0
    elif greeting[:1] == "h":
        amount = 20
    else:
        amount = 100
    return amount


if __name__ == "__main__":
    main()
