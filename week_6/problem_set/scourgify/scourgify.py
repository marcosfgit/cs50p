import sys
import csv

students = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name_list = row["name"].split(",")
                    first = name_list[1].strip()
                    last = name_list[0].strip()
                    house = row["house"]
                    students.append({"first": first, "last": last, "house": house})
        except FileNotFoundError:
            sys.exit("Could not read 1.csv")

        with open(sys.argv[2], "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)

