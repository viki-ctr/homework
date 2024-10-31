from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    if len(card_number_str) == 16:              #проверка корректности номера карты
        return f"{card_number_str[-16:-12]} {card_number_str[-12:-10]}** **** {card_number_str[-4:]} "
    else:
        return "Please enter a valid value"


print(get_mask_card_number)


def get_mask_account(account_number: Union[str | int]) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number)
    if len(account_number_str) == 20:   #проверка корректности номера счета
        return f"**{account_number_str[-4:]}"
    else:
        return "Please enter a valid value"
