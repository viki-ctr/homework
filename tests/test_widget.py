import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "type_of_payment, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("", "Введите корректные значения"),
        (" ", "Введите корректные значения"),
        ("Visa Platinum", "Введите корректные значения"),
        ("Goffj 7158300734726758", "Введите корректные значения"),
        ("ет 35383033474447895560", "Введите корректные значения"),
        ("64686473678894779589", "Введите корректные значения"),
    ],
)
def test_mask_account_card(type_of_payment: str, expected: str) -> str:
    assert mask_account_card(type_of_payment) == expected


def test_get_date() -> None:
    assert get_date("2024-11-19T12:34:56.789") == "19.11.2024"
    assert get_date("15-01-2022T12:30:45") == "15.01.2022"
    assert get_date(["2024", "11", "19"]) == "19.11.2024"
    assert get_date("Некорректная дата") == " Ошибка при обработке даты: Unknown string format: Некорректная дата"
