import pytest

def test_should_fail():
    a = 1
    b = 2
    assert a == b


def test_should_pass():
    a = 1
    b = 1
    assert a == b


pytest.main()