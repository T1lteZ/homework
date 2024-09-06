import json
import os


PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", 'data', 'operations.json')


def operation_list():
    """Функция принимает на вход JSON-файл и возвращает список операций"""
    try:
        with open(PATH_TO_FILE, "r", encoding="utf-8") as operation:
            try:
                operation_list_ = json.load(operation)
                return operation_list_
            except json.JSONDecodeError:
                operation_list_ = []
                return operation_list_
    except FileNotFoundError:
        operation_list_ = []
        return operation_list_
