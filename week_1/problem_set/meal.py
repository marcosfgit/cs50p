def main():
    time = input("What time is it? ").strip()
    time_converted = convert(time)
    if 7 <= time_converted <= 8:
        print("breakfast time")
    elif 12 <= time_converted <= 13:
        print("lunch time")
    elif 18 <= time_converted <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes_converted = float(minutes) / 60
    hours_converted = float(hours) + minutes_converted
    return hours_converted


if __name__ == "__main__":
    main()
