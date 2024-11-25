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
            raise ValueError("Невалидные значения")
    except StopIteration:
        print("Введите новые данные")
        return


def transaction_descriptions(transactions_list: list[dict[Any, Any]]) -> Generator[Any, None, None]:
    """Функция, принимающая список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    try:
        if len(transactions_list) > 0:
            for x in transactions_list:
                yield x["description"]
        if transactions_list == [None]:
            raise KeyError("Невалидные значения")
        else:
            raise KeyError("Невалидные значения")
    except StopIteration:
        print("Введите новые данные")
        return


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise NameError("Ошибка типа данных")
    if start > stop:
        raise ValueError("Невалидные значения")
    if start == 0:
        raise ValueError("Невалидные значения")
    else:
        for number in range(start, stop + 1):
            number_str = str(number)
            if len(number_str) < 16:
                card_number = "0" * (16 - len(number_str)) + number_str
                yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
            if len(number_str) == 16:
                card_number = number_str
                yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
    return
