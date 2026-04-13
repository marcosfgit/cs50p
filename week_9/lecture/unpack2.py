# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(galleons=100, sickles=50, knuts=25), "Knuts")

# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

print(total(**coins), "Knuts")