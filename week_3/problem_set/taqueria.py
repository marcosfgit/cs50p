dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

try:
    while True:
        item = input("Item: ").lower().title()
        if item in dict:
            item_cost = float(dict[item])
            total = total + item_cost
            print(f"${total:.2f}", sep="")
except EOFError:
    print()
    pass

