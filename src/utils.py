import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "data", "operations.json")


def transaction(file=file_path):
    """Функция, принимающая путь до JSON-файла и возвращающая список словарей или пустой список"""
    with open(file, "r", encoding="UTF-8") as f:
        try:
            transactions_list = json.load(f)
            if len(transactions_list) == 0:
                return []
            else:
                return transactions_list
        except json.JSONDecodeError:
            return []


# data = transaction(file=file_path)
# print(data)
