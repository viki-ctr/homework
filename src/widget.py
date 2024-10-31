from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_of_payment: Union[str]) -> str:
    """Функция, обрабатывающая информацию о картах и счетах"""
    if "Счет" in type_of_payment:
        bank_account = type_of_payment[-20:]
        return "Счет " + get_mask_account(bank_account)
    else:
        card_number_new = type_of_payment[-16:]
        card_details = type_of_payment.replace(card_number_new, "")
        return card_details + get_mask_card_number(card_number_new)


def get_date(info: Union[str]) -> str:
    """Функция, принимающая значение строки с датой в формате 'ДД.ММ.ГГГГ'"""
    date = info[0:10].split("-")
    return ".".join(date[::-1])
