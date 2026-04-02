# Say hello to the world
print("Hello, world")

# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str and capitalize user's name
name = name.strip().title()

# Say hello to user
print("Hello",name)
print("Hello ", end="")
print(name)
print("Hello ", name, sep="")
print(f"Hello {name}")
print()

# Use Quotes inside quotes
print('hello, "friend"')
print("hello, \"friend\"")
print()

"""
# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello {first}")
"""