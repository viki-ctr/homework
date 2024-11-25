from locale import currency

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_list, currency="USD"):
    gen = filter_by_currency(transactions_list, "USD")
    assert next(gen) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
    assert next(gen) == {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            }
    assert next(gen) == {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            }

    with pytest.raises(StopIteration):
        next(gen)


def test_filter_by_currency_invalid(transactions_list_invalid, currency="USD"):
    gen = filter_by_currency(transactions_list_invalid, "USD")
    assert next(gen) == "Введите нужную валюту"


def test_filter_by_currency_empty(transactions_list_empty, currency="USD"):
    gen = filter_by_currency(transactions_list_empty, "USD")
    with pytest.raises(ValueError) as exc_info:
        next(gen)
    assert str(exc_info.value) == "Невалидные значения"


def test_transaction_descriptions(transactions_list):
    gen = transaction_descriptions(transactions_list)
    assert next(gen) == "Перевод организации"


def test_transaction_descriptions_invalid(transactions_list_invalid):
    gen = transaction_descriptions(transactions_list_invalid)
    with pytest.raises(KeyError) as exc_info:
        next(gen)


def test_transaction_descriptions_empty(transactions_list_empty):
    gen = transaction_descriptions(transactions_list_empty)
    with pytest.raises(KeyError) as exc_info:
        next(gen)


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 11, ["0000 0000 0000 0001", "0000 0000 0000 0002",
                 "0000 0000 0000 0003", "0000 0000 0000 0004",
                 "0000 0000 0000 0005", "0000 0000 0000 0006",
                 "0000 0000 0000 0007", "0000 0000 0000 0008",
                 "0000 0000 0000 0009", "0000 0000 0000 0010",
                 "0000 0000 0000 0011"])
    ]
)
def test_card_number_generator(start, stop, expected_numbers):
    number = list(card_number_generator(1, 11))
    assert number == expected_numbers


def test_card_number_generator_finally():
    number = card_number_generator(9999999999999998, 9999999999999999)
    assert next(number) == "9999 9999 9999 9998"
    assert next(number) == "9999 9999 9999 9999"


def test_card_number_generator_finally_else():
    number = card_number_generator(9999999999999999, 10000000000000000000)
    assert next(number) == "9999 9999 9999 9999"


@pytest.mark.parametrize(
    "start, end, expected_numbers",
    [
        (100, 101, ["0000 0000 0000 0100", "0000 0000 0000 0101"]),
        (102, 103, ["0000 0000 0000 0102", "0000 0000 0000 0103"]),
    ]
)
def test_card_gen_use_parametrize(start, end, expected_numbers):
    result = list(card_number_generator(start, end))
    assert result == expected_numbers


def test_card_gen_invalid_parameters():
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(2, 1))


def test_card_gen_invalid_type():
    with pytest.raises(NameError) as exc_info:
        list(card_number_generator(a, 1))


def test_card_gen_none():
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(0, 1))


def test_card_gen_invalid_name():
    with pytest.raises(NameError) as exc_info:
        list(card_number_generator(a, b))

