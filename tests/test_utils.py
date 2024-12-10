from unittest.mock import MagicMock, patch

from mypy.util import json_dumps

from src.utils import transaction


@patch('builtins.open')
def test_transaction_from_json(mock_open: MagicMock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json_dumps([{"test": "test"}])
    assert transaction(mock_file) == [{"test": "test"}]
    mock_file.read.return_value = json_dumps({})
    assert transaction(mock_file) == []
    mock_file.read.return_value = ""
    assert transaction(mock_file) == []

