# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(1, 4) == 5
    assert add(3, 2) == 5
    assert add(5, 4) == 9
