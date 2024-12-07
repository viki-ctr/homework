import json


def transaction(file="C:/Users/vikas/py_prj/homework/data/operations.json"):
    """Функция, принимающая путь до JSON-файла и возвращающая список словарей или пустой список"""
    empty_list = []
    with open(file, "r", encoding="UTF-8") as f:
        try:
            transactions_list = json.load(f)
            if len(transactions_list) == 0:
                return empty_list
            else:
                empty_list.append(transactions_list)
                return empty_list
        except json.JSONDecodeError:
            return empty_list


data = transaction(file="C:/Users/vikas/py_prj/homework/data/operations.json")
# print(transaction())
