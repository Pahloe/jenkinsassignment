import pytest
from src.calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1, 3) == 4

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0

if __name__ == "__main__":
    pytest.main()