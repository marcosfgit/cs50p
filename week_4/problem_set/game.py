import random

while True:
    try:
        n_level = int(input("Level: "))
        if n_level > 0:
            break
    except ValueError:
        continue

n_random = random.randint(1, n_level)

while True:
    try:
        n_guess = int(input("Guess: "))
        if n_guess < 1:
            continue
    except ValueError:
        continue

    if n_guess < n_random:
        print("Too small!")
        continue
    elif n_guess > n_random:
        print("Too large!")
        continue
    else:
        print("Just right!")
        break
