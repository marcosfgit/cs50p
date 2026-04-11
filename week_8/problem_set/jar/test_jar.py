from jar import Jar
import pytest


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5

    jar_default = Jar()
    assert jar_default.capacity == 12

    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(2)

    assert jar.size == 2

    jar.deposit(3)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)

    jar.withdraw(3)
    assert jar.size == 7

    jar.withdraw(7)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)
