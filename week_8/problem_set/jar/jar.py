class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.capacity >= (self.size + n):
            self._size = self._size + n
            return self._size
        else:
            raise ValueError("The jar can't handle more cookies!")

    def withdraw(self, n):
        if (self.size - n) >= 0:
            self._size = self._size - n
            return self._size
        else:
            raise ValueError("Don't be greedy! There aren't that many cookies left.")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(15)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)
    print(f"Capacity: {jar.capacity}")
    print(f"Cookies in the jar: {jar.size}")


if __name__ == "__main__":
    main()
