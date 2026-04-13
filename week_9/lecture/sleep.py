# n = int(input("What's n? "))
# for i in range(n):
#     print("🐑" * i)

#####

# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print(sheep(i))


# def sheep(n):
#     return "🐑" * n


# if __name__ == "__main__":
#     main()

#####


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()

# with this program, if we do n = 1000000, the program doesn't run, we have to use generators (yield)