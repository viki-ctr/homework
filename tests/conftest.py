import pytest
from time import time
import pandas as pd


@pytest.fixture
def empty_line_card():
    return ' '


@pytest.fixture
def none_number():
    return ''


@pytest.fixture
def test_dict_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def test_dict_list_incorrect_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '12/09/2017 21;42'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'четырнадцатое октября две тысячи восемнадцатого года'}]


@pytest.fixture
def test_dict_list_incorrect_date_second():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'четырнадцатое октября две тысячи восемнадцатого года'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '12/09/2017 21;42'}]


@pytest.fixture
def transactions_list():
    return (
        [
            {
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
            },
            {
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
            },
            {
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
            },
        ]
    )


@pytest.fixture
def transactions_list_invalid():
    return (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "GBP",
                        "code": "GBP"
                    }
                },
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "BYN"
                    }
                },
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "RUB",
                        "code": "RUB"
                    }
                },
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )


@pytest.fixture
def transactions_list_empty():
    return []


@pytest.fixture
def time_for_test():
    time_1 = time()
    time_2 = time()
    return time_1, time_2


@pytest.fixture
def test_csv_xlsx() -> pd.DataFrame:
    test_dict = {

        "id": [650703.0, 3598919.0],

        "state": ["EXECUTED", "EXECUTED"],

        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],

        "amount": [16210.0, 29740.0],

        "currency_name": ["Sol", "Peso"],

        "currency_code": ["PEN", "COP"],

        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],

        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],

        "description": ["Перевод организации", "Перевод с карты на карту"]

    }
    return pd.DataFrame(test_dict)
