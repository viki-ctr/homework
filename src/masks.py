from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    if card_number_str == card_number_str.isdigit():              #проверка корректности номера карты
        return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]} "
    else:
        return "Please enter a valid value"


print(get_mask_card_number)


def get_mask_account(account_number: Union[str | int]) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number)
    if account_number_str == account_number_str.isdigit() and len(account_number_str) == 16:   #проверка корректности номера счета
        return f"**{account_number_str[-4:]}"
    else:
        return "Please enter a valid value"


print(get_mask_account)
