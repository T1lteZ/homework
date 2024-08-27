import pytest

from src.decorators import log, my_function


def test_log_1():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_2():
    with pytest.raises(UnboundLocalError, match="cannot access local variable 'result' where it is not associated with a value"):
        my_function()


def test_log_3():
    with pytest.raises(UnboundLocalError, match="cannot access local variable 'result' where it is not associated with a value"):
        my_function(1, "2")


def test_log_4():
    assert my_function(1, 0) == 1