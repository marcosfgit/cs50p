def main():
    x = input()
    y = convert(x)
    print(y)

def convert(x):
    x = x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    return x

main()
