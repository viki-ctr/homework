import pytest

from src.decorators import my_function


def test_successful_execution(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert 'my_function' in captured.out


def test_error_handling(capsys):
    with pytest.raises(expected_exception=Exception):
        my_function(1, 'a')
    captured = capsys.readouterr()
    assert "" in captured.out




