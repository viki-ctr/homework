from typing import Iterable, Any


def filter_by_state(dictionaries: Iterable[list[dict[Any]]], state = 'EXECUTED') -> list:
    """Функция для выведения данных по определенному значению"""
    executed_list = []
    for i in dictionaries:
        if i['state'] == state:
            executed_list.append(i)
    return executed_list


def sort_by_date(dictionaries: Iterable[list[dict[Any]]], reverse = True) -> list:
    """Функция для сортировки по датам"""
    list_for_date = sorted(dictionaries, key=lambda x: x['date'], reverse=True)
    return list_for_date
