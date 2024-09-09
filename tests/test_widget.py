import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card(numbers_acc_card, numbers_acc_, numbers_card_zero):
    assert mask_account_card("Visa Platinum 7000792289606361") == numbers_acc_card

    assert mask_account_card("Счет 73654108430135874305") == numbers_acc_


@pytest.mark.parametrize("values, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2003-10-10T03:36:48.443322", "10.10.2003")
])
def test_get_date(values, expected):
    assert get_date(values) == expected
