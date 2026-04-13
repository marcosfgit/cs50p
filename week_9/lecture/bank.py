balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance # you have to call global variable and this way you can change it, not only read it
    balance += n


def withdraw(n):
    global balance # you have to call global variable and this way you can change it, not only read it
    balance -= n


if __name__ == "__main__":
    main()