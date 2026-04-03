expression = input("Expression: ").strip().split(" ")

x = int(expression[0])
y = expression[1]
z = int(expression[2])

if y == "+":
    print(f"{(x + z):.1f}")
elif y == "-":
    print(f"{(x - z):.1f}")
elif y == "*":
    print(f"{(x * z):.1f}")
elif y == "/":
    print(f"{(x / z):.1f}")

