from src.mask import get_mask_card_number, get_mask_account


def test_mask_card(numbers_card, numbers_card_error, numbers_card_zero):
    assert get_mask_card_number("7000792289606361") == numbers_card

    assert get_mask_card_number("777777777777") == numbers_card_error

    assert get_mask_card_number("") == numbers_card_zero


def test_mask_acc(numbers_acc, numbers_card_error, numbers_card_zero):
    assert get_mask_account("73654108430135874305") == numbers_acc

    assert get_mask_account("7777777777") == numbers_card_error

    assert get_mask_account("") == numbers_card_zero
