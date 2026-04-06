"""
import random

coin = random.choice(["heads", "tails"])

print(coin)
"""

from random import choice
from random import randint
from random import shuffle

coin = choice(["heads", "tails"])

print(coin)
print()

#

number = randint(1, 10)

print(number)
print()

#

cards = ["jack", "queen", "king"]

shuffle(cards)

for card in cards:
    print(card)