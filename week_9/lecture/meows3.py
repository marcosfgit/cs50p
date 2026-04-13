def meow(n: int): # : int is a type hint
    for _ in range(n):
        print("meow")


number: int = int(input("Number: ")) # : int is a type hint
meow(number)

# run mypy meows3.py in the terminal