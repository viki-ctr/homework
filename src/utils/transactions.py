import json
import os
from typing import Any


def transaction(file: Any) -> list[Any]:
    """Функция, принимающая путь до JSON-файла и возвращающая список словарей или пустой список"""
    empty_list = []
    with open(os.path.abspath(file), "r") as file:
        try:
            transactions_list = json.loads(file)
            if len(transactions_list) == 0 or isinstance(transactions_list, list):
                return empty_list
            else:
                empty_list.append(transactions_list)
                return empty_list
        except json.JSONDecodeError:
            return empty_list


if __name__ == "__main__":
    path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
