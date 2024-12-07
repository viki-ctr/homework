from unittest.mock import Mock, patch

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


def test_failed_status_code():
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.return_value = "Запрос не был успешным. Возможная причина: Bad Request"
    result = transaction_amount({'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}})
    assert result == "Запрос не был успешным. Возможная причина: Bad Request"


# @patch('src.external_api.requests.get')
# def test_transaction_usd(mocked_get):
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value = 616804.608265
#     result = transaction_amount({'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}})
#     assert result == 616804.608265