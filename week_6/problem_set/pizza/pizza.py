import sys
import csv
from tabulate import tabulate

table = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for name, small, large in reader:
                    table.append([name, small, large])
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")

