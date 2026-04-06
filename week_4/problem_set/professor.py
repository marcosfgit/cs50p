import random


def main():
    level = get_level()
    score = 0

    for sum in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        count = 0

        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == x + y:
                    score = score + 1
                    break
                elif guess != x + y:
                    print("EEE")
                    count = count + 1
                    if count == 3:
                        z = x + y
                        print(f"{x} + {y} = {z}")
                        break

            except ValueError:
                print("EEE")
                count = count + 1
                if count == 3:
                    z = x + y
                    print(f"{x} + {y} = {z}")
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level in [1 ,2 ,3]:
        if level == 1:
            n = random.randint(0, 9)
        elif level == 2:
            n = random.randint(10, 99)
        elif level == 3:
            n = random.randint(100, 999)
    else:
        raise ValueError
    return n


if __name__ == "__main__":
    main()
