import os
import sys
sys.path.append(os.getcwd())
from src.widget import get_date, mask_account_card
from src.bank_operations import search_bank_operation
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.financy import csv_reader_func, xlsx_reader_func
from src.utils import operation_list


PATH_TO_FILE_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
PATH_TO_FILE_CSV = "C:/Users/stasf/PycharmProjects/homework/financy.csv"
PATH_TO_FILE_XLSX = "C:/Users/stasf/PycharmProjects/homework/transactions_excel.xlsx"


def main_menu():
    while True:
        menu_start = int(input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
                        Выберите необходимый пункт меню:
                        1. Получить информацию о транзакциях из JSON-файла
                        2. Получить информацию о транзакциях из CSV-файла
                        3. Получить информацию о транзакциях из XLSX-файла"""))

        if menu_start == 1:
            print("Для обработки выбран JSON-файл.")
            operations = operation_list(PATH_TO_FILE_JSON)
            break
        elif menu_start == 2:
            print("Для обработки выбран CSV-файл.")
            operations = csv_reader_func(PATH_TO_FILE_CSV)
            break
        elif menu_start == 3:
            print("Для обработки выбран XLSX-файл.")
            operations = xlsx_reader_func(PATH_TO_FILE_XLSX)
            break
        elif menu_start != 1 or 2 or 3:
            print("Неверно выбранна функция.")

    status_list = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        operation_status = str(input("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.""").upper())

        if operation_status not in status_list:
            print(f"Статус операции {operation_status} недоступен.")
            operation_status = input("Попробуйте снова")
            if operation_status in status_list:
                print(f"Выбор {operation_status}")
            else:
                break
        else:
            print(f"Выбор {operation_status}")
            break

        filtered_transactions = filter_by_state(operations, state=operation_status)

        date_sorted = input("Отсортировать операции по дате? Да/Нет. ").lower()
        if date_sorted == "да":
            date_sort_t_f = input("Отсортировать по возрастанию или по убыванию?").lower()
            if date_sort_t_f == "по возрастанию":
                date_flag = False
            else:
                date_flag = True
        elif date_sorted == "нет":
            continue
        else:
            continue
        filtered_transactions = sort_by_date(filtered_transactions, date_flag)

        next_choice_rub = """Выводить только рублевые тразакции? Да/Нет"""
        input_user_rub = input(f"{next_choice_rub}\n").lower()
        while input_user_rub not in ["да", "нет"]:
            print("\nВвели некорректную сортировку\nПопробуйте еще раз:")
            input_user_rub = input(f"{next_choice_rub}\n").lower()
            if input_user_rub == "да":
                filtered_transactions = filter_by_currency(filtered_transactions, "RUB")

        filtered_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower
        if filtered_by_word == "да":
            word = input("Введите слово...")
            filtered_transactions = search_bank_operation(filtered_transactions, word)
        else:
            print(" ")

        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        if menu_start == 1:
            for transaction in filtered_transactions:
                description = transaction.get("description")
                if description == "Открытие вклада":
                    from_ = description
                else:
                    from_ = mask_account_card(transaction.get("from"))

                to_ = mask_account_card(transaction.get("to"))
                date = get_date(transaction.get("date"))

                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["code"]

                if description == "Открытие вклада":
                    print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
                else:
                    print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
        else:
            for transaction in filtered_transactions:
                description = transaction.get("description")
                if description == "Открытие вклада":
                    from_ = description
                else:
                    from_ = mask_account_card(transaction.get("from"))

                date = get_date(transaction.get("date"))


                amount = transaction.get("amount")
                currency = transaction.get("currency_name")

                if description == "Открытие вклада":
                    to_ = mask_account_card(transaction.get("to"))
                    print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
                else:
                    to_ = mask_account_card(transaction.get("to"))
                    print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
        break

main_menu()