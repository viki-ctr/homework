import re
from collections import Counter
from datetime import datetime
from typing import Any, Iterable

from dateutil import parser


def filter_by_state(dictionaries: Iterable[dict], state: Any = "EXECUTED") -> list[dict]:
    """Функция для выведения данных по определенному значению"""
    executed_list = []
    for meaning in dictionaries:
        if meaning.get("state") == state:
            executed_list.append(meaning)
    return executed_list


def sort_by_date(dictionaries: Iterable[dict], reverse: bool = True) -> list[dict]:
    """Функция для сортировки по датам"""

    def parse_date(item):
        date_str = item.get("date")
        if not date_str:
            return datetime.min
        try:
            return parser.parse(date_str)
        except (ValueError, TypeError):
            print(f"Предупреждение: некорректный формат даты '{date_str}'.")
            return datetime.min

    return sorted(dictionaries, key=parse_date, reverse=reverse)


def search_operations(transactions: list[dict], search_bar: str) -> list[dict]:
    """Функцию, принимающая список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей с данной строкой"""
    try:
        search_list = []
        for transaction in transactions:
            if re.search(search_bar, transaction.get("description", ""), flags=re.IGNORECASE):
                search_list.append(transaction)
            else:
                continue
        return search_list
    except (ValueError, TypeError):
        print("По вашему запросу ничего не найдено")


def count_categories(transactions: list[dict]) -> dict:
    """Функция, принимающая список словарей, возвращает словарь,
    где ключ - название категорий, значение - кол-во операций"""
    categories = []
    for transaction in transactions:
        categories.append(transaction["description"])
    counted = dict(Counter(categories))
    return counted


transa = [
    {
        "id": 939719570,
        "state": "CANCELED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
]
trans = 12324
# print(search_operations(transa, "Перевод с карты на карту"))
# print(count_categories(transa))
# print(sort_by_date(transa, reverse=False))
