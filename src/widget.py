from datetime import datetime as dt
from typing import Union

from dateutil import parser

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_of_payment: str) -> str:
    """Функция, обрабатывающая информацию о картах и счетах"""
    name_card = ["Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"]
    if len(type_of_payment) > 21:
        type_of_payment_list = type_of_payment.split()
        number_date = type_of_payment_list[-1]
        del type_of_payment_list[-1]
        type_of_payment_join = " ".join(type_of_payment_list)
        if type_of_payment_join in name_card:
            return type_of_payment_join + " " + get_mask_card_number(number_date)
        elif "Счет" in type_of_payment_join:
            return "Счет " + get_mask_account(number_date)
        else:
            return "Введите корректные значения"
    elif type_of_payment == "":
        return "Введите корректные значения"
    else:
        return "Введите корректные значения"


def get_date(info: Union[str, list]) -> str:
    """Функция, принимающая значение строки с датой и возвращающая её в формате 'дд.мм.гггг'."""

    try:

        # Если передана строка, пытаемся парсить её

        if isinstance(info, str):

            # Если формат известен

            try:

                parsed_date = dt.strptime(info, "%Y-%m-%dT%H:%M:%S.%f")

            except ValueError:

                # Если формат неизвестен, используем парсер

                parsed_date = parser.parse(info)

        elif isinstance(info, list):

            # Если передан список, объединяем элементы и пытаемся парсить как строку

            parsed_date = parser.parse("-".join(info))

        else:

            return "Неверный формат данных"

        # Возвращаем дату в нужном формате
        return parsed_date.strftime("%d.%m.%Y")
    except Exception as e:
        return f"Ошибка при обработке даты: {e}"


# print(mask_account_card('Maestro 1596837868705199'))
# print(get_date("2024-11-19T12:34:56.789"))
