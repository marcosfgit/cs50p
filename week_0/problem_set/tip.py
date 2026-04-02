def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_remove = d.replace("$","")
    d_float = round(float(d_remove),1)
    return d_float


def percent_to_float(p):
    p_remove = p.replace("%","")
    p_float = float(p_remove)*0.01
    return p_float


main()
