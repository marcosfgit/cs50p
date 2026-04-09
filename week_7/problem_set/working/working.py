import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s):
        # First hour
        first_hour = int(match.group(1))

        # First minute
        if match.group(2):
            first_minute = match.group(2)
        else:
            first_minute = ":00"

        # First meridian
        first_meridian = match.group(3)
        if first_meridian == "PM" and first_hour != 12:
            first_hour = first_hour + 12
        elif first_meridian == "AM" and first_hour == 12:
            first_hour = 0

        # Second hour
        second_hour = int(match.group(4))

        # Second minute
        if match.group(5):
            second_minute = match.group(5)
        else:
            second_minute = ":00"

        # Second meridian
        second_meridian = match.group(6)
        if second_meridian == "PM" and second_hour != 12:
            second_hour = second_hour + 12
        elif second_meridian == "AM" and second_hour == 12:
            second_hour = 0

        # Return value
        return f"{first_hour:02}{first_minute} to {second_hour:02}{second_minute}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
