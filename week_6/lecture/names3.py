"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
"""

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())