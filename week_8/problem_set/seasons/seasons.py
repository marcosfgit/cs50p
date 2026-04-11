from datetime import date
import sys
import re
import inflect


def main():
    print(convert(input("Date of Birth: ")))


def convert(s):
    matches = re.search(r"^([1][0-9]{3}|[2][0][0-1][0-9]|[2][0][2][0-6])-([0][1-9]|[1][0-2])-([0][1-9]|[1-2][0-9]|30|31?$)", s)
    if not matches:
        sys.exit("Invalid date")

    convert_date = date.fromisoformat(s)
    today = date.today()
    diff = today - convert_date
    days = diff.days
    total_minutes = int(days * 24 * 60)

    p = inflect.engine()
    date_words = p.number_to_words(total_minutes, andword="").capitalize()
    
    return f"{date_words} minutes"


if __name__ == "__main__":
    main()
