import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions,filter_list_trans):
    result = filter_by_currency(transactions, "USD")
    assert next(result) == filter_list_trans


def test_filter_by_currency_zero(zero_trans):
    result = filter_by_currency(zero_trans, "USD")
    assert next(result) == "Нет транзакций"


def test_transaction_descriptions(transactions):
    results = transaction_descriptions(transactions)
    assert next(results) == "Перевод организации"

    assert next(results) == "Перевод со счета на счет"

    assert  next(results) == "Перевод со счета на счет"

    assert next(results) == "Перевод с карты на карту"

    assert next(results) == "Перевод организации"


def test_transaction_description_zero(zero_trans):
    result = transaction_descriptions(zero_trans)
    assert next(result) == "Нет транзакций"


def test_card_number_generator(start=1, end=5):
    generator_number = card_number_generator(1, 5)
    assert next(generator_number) == "0000 0000 0000 0001"

    assert next(generator_number) == "0000 0000 0000 0002"

    assert next(generator_number) == "0000 0000 0000 0003"

    assert next(generator_number) == "0000 0000 0000 0004"

    assert next(generator_number) == "0000 0000 0000 0005"