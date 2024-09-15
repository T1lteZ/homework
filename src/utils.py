import json
import logging
import os
from json import JSONDecodeError
from typing import Any

from src.external_api import conversion_api

current_dir = os.path.dirname(os.path.abspath(__file__))


file_path_rel = os.path.join(current_dir, "../logs/utils.log")
file_path_abs = os.path.abspath(file_path_rel)


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(file_path_abs, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def operation_list(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="utf-8") as financial_file:
            try:
                logger.info("Файл найден")
                transactions = json.load(financial_file)
            except JSONDecodeError:
                return []
        if not isinstance(transactions, list):
            logger.info("Импортируемый список пуст")
            return []
        return transactions
    except FileNotFoundError:
        logger.info("Файл не найден")
        return []


def sum_operation_on_rub(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = conversion_api(trans)
    return amount
