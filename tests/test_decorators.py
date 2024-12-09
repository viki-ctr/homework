import pytest

from src.decorators import log, my_function


def test_log(capsys):
    @log(filename="logs/mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    result = ''
    answer = captured.out.rstrip()


    assert result in answer


def test_error_handling(capsys):
    with pytest.raises(expected_exception=Exception):
        my_function(1, 'a')
    captured = capsys.readouterr()
    assert '' in captured.out



