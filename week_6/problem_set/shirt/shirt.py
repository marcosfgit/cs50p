import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].lower().endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid input")
    elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
        sys.exit("Input and output have different extensions")
    else:
        try:
            photo = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            photo_resize = ImageOps.fit(photo, shirt.size)
            photo_resize.paste(shirt, shirt)
            photo_resize.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")
