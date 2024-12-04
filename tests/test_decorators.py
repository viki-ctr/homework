from time import time

import pytest
from mypy.types import NoneTyp

from src.decorators import log, my_function


def test_log(capsys):
    @log(filename="logs/mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    time_1 = time()
    time_1_round = round(time_1, 1)
    time_2 = time()
    time_2_round = round(time_2, 1)
    result = f'my_function ok. \nStart time: {time_1_round}. \nEnd time: {time_2_round}.'
    answer = captured.out.rstrip()


    assert result in answer


def test_error_handling(capsys):
    with pytest.raises(expected_exception=Exception):
        my_function(1, 'a')
    captured = capsys.readouterr()
    assert '' in captured.out


@log(filename="testdecor.txt")
def test_error_function_with_file(*args, **kwargs):
    raise ValueError("Something went wrong!")
