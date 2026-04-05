while True:
    try:
        fraction = input("Fraction: ")
        fraction_split = fraction.split("/")
        x = int(fraction_split[0])
        y = int(fraction_split[1])
        if x <= y and x >= 0 and y != 0:
            percentage = int(round((x / y * 100), 0))
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if 99 <= percentage <= 100:
    print("F")
elif 1 < percentage < 99:
    print(percentage, "%", sep="")
elif 0 <= percentage <= 1:
    print("E")
