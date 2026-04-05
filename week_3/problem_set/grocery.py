item_dict = {}

try:
    while True:
        item = input()
        if item in item_dict:
            item_dict[item] = item_dict[item] + 1
        else:
            item_dict[item] = 1
except EOFError:
    pass

item_dict = dict(sorted(item_dict.items()))

for item in item_dict:
    print(item_dict[item], item.upper())

