import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import empty_line_card, none_number


@pytest.mark.parametrize(
    'card_number, expected',
    [
        ('7000792289606361', '7000 79** **** 6361'),
        ('565657dfdf5656', 'Please enter a valid value'),
        ('73654108430135874305', 'Please enter a valid value'),
        ('ghghghghghghghgh', 'Please enter a valid value'),
        ('', 'Please enter a valid value'),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    'account_number, expected',
    [
        ('7000792289606361', 'Please enter a valid value'),
        ('565657dfdf5656', 'Please enter a valid value'),
        ('73654108430135874305', '**4305'),
        ('ghghghghghghghgh', 'Please enter a valid value'),
        (' ', 'Please enter a valid value'),
    ],
)
def test_get_mask_account(account_number: str, expected: str):
    assert get_mask_account(account_number) == expected


def test_get_mask_card_number_empty():
    assert get_mask_card_number(empty_line_card) == 'Please enter a valid value'


def test_get_mask_account_none():
    assert get_mask_account(none_number) == 'Please enter a valid value'
