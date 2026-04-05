months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


try:
    while True:
        date = input("Date: ")
        if "/" in date:
            date = date.split("/")
            if date[0] in months:
                continue
            month_number = int(date[0])
            if month_number > 12 or month_number < 1:
                continue
            year_number = int(date[2])
            day_number = int(date[1])
            if day_number > 31 or day_number < 1:
                continue
            print(f"{year_number:04}-{month_number:02}-{day_number:02}")
            break

        elif "," in date:
            date = date.split(" ")
            if date[0] not in months:
                continue
            month_number = months.index(date[0]) + 1
            if month_number > 12 or month_number < 1:
                continue
            year_number = int(date[2])
            day_number = int(date[1].replace(",", ""))
            if day_number > 31 or day_number < 1:
                continue
            print(f"{year_number:04}-{month_number:02}-{day_number:02}")
            break

        else:
            continue

except (ValueError, IndexError):
    pass
