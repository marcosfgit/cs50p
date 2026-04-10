#def main():
#    name = get_name()
#    house = get_house()
#    print(f"{name} from {house}")


#def get_name():
#    return input("Name: ")


#def get_house():
#    return input("House: ")


#if __name__ == "__main__":
#    main()


#####


# def main():
#     student = get_student() # student is the tuple (name, house)
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house # this returns a tuple


# if __name__ == "__main__":
#     main()


def main():
    student = get_student() # student is the list [name, house]
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] # this returns a list


if __name__ == "__main__":
    main()