i = 50

print("Amount Due:", i)

while i > 0:
    j = int(input("Insert Coin: "))
    if j == 25 or j == 10 or j == 5:
        i = i - j
        if i > 0:
            print("Amount Due:", i)
    else:
        print("Amount Due:", i)

if i == 0:
    print("Change Owed:", i)
else:
    print("Change Owed:", -i)

