from typing import Any, Iterable


def filter_by_state(dictionaries: Iterable[dict], state: Any = "EXECUTED") -> list[dict]:
    """Функция для выведения данных по определенному значению"""
    executed_list = []
    for meaning in dictionaries:
        if meaning["state"] == state:
            executed_list.append(meaning)
    return executed_list


def sort_by_date(dictionaries: Iterable[dict], reverse: bool = True) -> list[dict]:
    """Функция для сортировки по датам"""
    list_for_date = sorted(dictionaries, key=lambda x: x["date"], reverse=reverse)
    return list_for_date
