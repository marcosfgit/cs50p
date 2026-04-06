from pyfiglet import Figlet
import sys

figlet = Figlet()
list_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    str = input("Input: ")
    f = figlet.renderText(str)
    print("Output: \n", f)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in list_fonts:
    str = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    f = figlet.renderText(str)
    print("Output: \n", f)

else:
    sys.exit("Invalid usage")
