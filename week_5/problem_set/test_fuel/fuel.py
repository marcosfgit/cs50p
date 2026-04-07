def main():
    while True:
        fraction = input("Fraction: ")
        try:
            convertion = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(convertion))


def convert(fraction):
    fraction_split = fraction.split("/")
    x = int(fraction_split[0])
    y = int(fraction_split[1])
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    if x < 0:
        raise ValueError
    if x <= y and x >= 0 and y != 0:
        percentage = int(round((x / y * 100), 0))
        return percentage


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    elif 0 <= percentage <= 1:
        return "E"


if __name__ == "__main__":
    main()
