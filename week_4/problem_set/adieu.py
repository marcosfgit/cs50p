import inflect

p = inflect.engine()

list_names = []

try:
    while True:
        name = input("Name: ")
        list_names.append(name)
        
except EOFError:
    print("\nAdieu, adieu, to", p.join(list_names))
