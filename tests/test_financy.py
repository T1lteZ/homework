from unittest.mock import mock_open, patch

from src.financy import csv_reader_func, xlsx_reader_func


@patch("src.financy.pd.read_csv")
def test_read_csv(mock_read, test_df):
    mock_read.return_value = test_df

    result = csv_reader_func("C:/Users/stasf/PycharmProjects/homework/data/test_transactions.csv")

    expected = test_df

    assert result == expected


def test_csv_none():
    assert csv_reader_func("") == []


@patch("src.financy.pd.read_excel")
def test_read_excel(mock_read, excel_test):
    mock_read.return_value = excel_test
    result = xlsx_reader_func("C:/Users/stasf/PycharmProjects/homework/excel_test.xlsx")

    expected = excel_test

    assert result == expected


def test_excel_none():
    assert xlsx_reader_func("") == []
