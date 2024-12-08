import pytest
import unittest
from unittest.mock import MagicMock, patch, Mock
import requests

from src.external_api import transaction_amount


def test_transaction_amount():
    assert transaction_amount({
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                }
            }) == 9824.07


@patch('src.external_api.requests.get')
def test_successful_status_code(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "info": {"rate": 1.0105},
    }
    mock_get.return_value = mock_response
    result = transaction_amount({'operationAmount': {'amount': '9824.07', 'currency': {'name': 'EUR', 'code': 'EUR'}}})
    assert result == 9825.08


def test_invalid_transaction_format():
        """Тест для некорректного формата транзакции"""
        transact = {
            "operationAmount": {
                "currency": {"code": "USD"}
            }
        }
        with pytest.raises(KeyError, match="Некорректный формат транзакции."):
            transaction_amount(transact)


def test_request_exception():
    with patch("src.external_api.requests.get", side_effect=requests.exceptions.RequestException):
        transact = {
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"}
            }
        }
        result = transaction_amount(transact)
        assert result is None
