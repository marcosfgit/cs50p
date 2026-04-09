from um import count
import pytest


def test_count_um():
    assert count("um") == 1
    assert count("Hello, um, world") == 1
    assert count("Hello, um, world, um") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
