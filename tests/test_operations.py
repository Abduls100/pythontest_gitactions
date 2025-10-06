from src.maths_operations import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(-2, 7) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 2) == 8
    assert subtract(-1, 8) == -9