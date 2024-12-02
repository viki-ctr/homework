import pytest

from src.decorators import my_function
from src.decorators import log


def test_successful_execution(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert 'my_function' in captured.out


def test_error_handling(capsys):
    with pytest.raises(expected_exception=Exception):
        my_function(1, 'a')
    captured = capsys.readouterr()
    assert '' in captured.out


@log(filename="testdecor.txt")
def test_error_function_with_file(*args, **kwargs):
    raise ValueError("Something went wrong!")

