import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def correct_card_number():
    return '7000792289606361'


@pytest.fixture
def card_number_with_letters():
    return '565657dfdf5656'


@pytest.fixture
def correct_account_number():
    return '73654108430135874305'


@pytest.fixture
def letters_in_card():
    return 'ghghghghghghghgh'


@pytest.fixture
def empty_line_card():
    return ' '


@pytest.fixture
def none_number():
    return ''


