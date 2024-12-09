import json


def transaction(file="C:/Users/vikas/py_prj/homework/data/operations.json"):
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


# data = transaction(file="C:/Users/vikas/py_prj/homework/data/operations.json")
print(transaction())
