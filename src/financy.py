import csv
from typing import Any

import pandas as pd


def csv_reader_func(path) -> Any:
    with open("financy.csv") as file:
        transaction_list = []
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            transaction_list.append(row)
        return transaction_list


print(csv_reader_func("C:/Users/stasf/PycharmProjects/homework/financy.csv"))


def xlsx_reader_func(path) -> Any:
    reader = pd.read_excel(path)
    dict_excel = reader.to_dict(orient="records")
    return dict_excel


print(xlsx_reader_func("C:/Users/stasf/PycharmProjects/homework/transactions_excel.xlsx"))