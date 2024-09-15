import csv
import logging
import os
from typing import Any

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))


file_path_rel = os.path.join(current_dir, "../logs/financy.log")
file_path_abs = os.path.abspath(file_path_rel)


logger = logging.getLogger("financy")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(file_path_abs, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def csv_reader_func(path) -> Any:
    """Функция чтения CSV"""
    try:
        with open(path) as file:
            logger.info("Файл найден")
            transaction_list = []
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transaction_list.append(row)
            return transaction_list
    except FileNotFoundError:
        logger.info("Файл не найден")
        return []


print(csv_reader_func("C:/Users/stasf/PycharmProjects/homework/financy.csv"))


def xlsx_reader_func(path) -> Any:
    """Функция чтения excel"""
    try:
        logger.info("Файл найден")
        reader = pd.read_excel(path)
        dict_excel = reader.to_dict(orient="records")
        return dict_excel
    except FileNotFoundError:
        logger.info("Файл не найден")
        return []


print(xlsx_reader_func("C:/Users/stasf/PycharmProjects/homework/transactions_excel.xlsx"))
