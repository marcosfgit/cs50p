import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1]) as file:
                lines = file.readlines()
            count = 0
            for line in lines:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                count = count + 1
            print(count)
        except FileNotFoundError:
            sys.exit("File does not exist")

