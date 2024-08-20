import pytest

from src.widget import mask_account_card


def mask_acc_card_num():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
