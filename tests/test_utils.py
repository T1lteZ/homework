import os
from unittest.mock import patch
import pytest

from src.utils import operation_list, sum_operation_on_rub


def test_financial_transactions_nofile():
    assert operation_list('nofile') == []


def test_financial_transactions(path):
    assert operation_list(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
             "name": "руб.",
             "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_empty_list(path_empty_list):
    assert operation_list(path_empty_list) == []


def test_financial_transactions_mistake_json(path_mistake_json):
    assert operation_list(path_mistake_json) == []


def test_transaction_amount(trans):
    assert sum_operation_on_rub(trans) == '31957.58'


@patch('src.utils.currency_conversion')
def test_transaction_amount_non_rub(mock_currency_conversion, trans_1):
    mock_currency_conversion.return_value = 1000.0
    assert sum_operation_on_rub(trans_1) == 1000.0