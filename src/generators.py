from typing import Any, Generator


def filter_by_currency(transactions_list: list[dict[Any, Any]], currency="USD") -> Generator[Any, None, None]:
    """Функция, принимающая на вход список словарей, представляющих транзакции"""
    try:
        if len(transactions_list) > 0:
            for x in transactions_list:
                if x["operationAmount"]["currency"]["code"] == currency:
                    yield x
                elif x["operationAmount"]["currency"]["code"] != currency:
                    yield "Введите нужную валюту"
                else:
                    yield "Проверьте корректность данных"
        else:
            return "Проверьте корректность данных"
    except StopIteration:
        print("Введите новые данные")


def transaction_descriptions(transactions_list: list[dict[Any, Any]]) -> Generator[Any, None, None]:
    """Функция, принимающая список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    try:
        if len(transactions_list) > 0:
            for x in transactions_list:
                yield x["description"]
        if transactions_list == [None]:
            return "Нет корректных данных"
        else:
            return "Проверьте корректность данных"
    except StopIteration:
        print("Введите новые данные")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if start > stop:
        raise ValueError("Невалидные значения")
    else:
        for number in range(start, stop):
            number_str = str(number)
            if len(number_str) < 16:
                card_number = "0" * (16 - len(number_str)) + number_str
            elif len(number_str) == 16:
                card_number = number_str
            else:
                return "Невалидные значения"
        yield f"{card_number[:4]} {card_number[4:9]} {card_number[8:13]} {card_number[13:]}"
