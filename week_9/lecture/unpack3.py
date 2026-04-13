def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


f(100, 50, 25)
print()
f(galleons=100, sickles=50, knuts=25)