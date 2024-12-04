from typing import Any
import re
from collections import defaultdict


def search_bank_operation(operation_list: list[dict], user_input: Any) -> list[dict]:
    """Функция поиска операций"""
    result_operation = []
    for bank_operation in operation_list:
        if re.search(user_input, bank_operation.get("description", "")):
            result_operation.append(bank_operation)
        return result_operation


def count_operation(operation_list: list[dict], category: list[str]) -> dict[str, int]:
    """Функция поиска операций по категориям"""
    category_count = defaultdict(int)
    for operation in operation_list:
        descrition = operation.get("description", "").lower()
        for categories in category:
            if re.search(re.escape(categories.lower()), descrition):
                category_count[categories] += 1
    return dict(category_count)
