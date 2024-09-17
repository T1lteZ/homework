import os
import sys
sys.path.append(os.getcwd())

from src.bank_operations import search_bank_operation
from src.generators import filter_by_currency
from src.mask import get_mask_account, get_mask_card_number
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

    while True:
        operation_status = input("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.""").upper()

        status_list = ["EXECUTED", "CANCELED", "PENDING"]
        if operation_status not in status_list:
            print(f"Операция {operation_status} не доступна.")
        else:
            break

        filtered_transactions = filter_by_state(operations, operation_status)

        date_sorted = input("Отсортировать операции по дате? Да/Нет. ").lower()
        if date_sorted == "да":
            date_sort_t_f = input("Отсортировать по возрастанию или по убыванию?").lower()
            if date_sort_t_f == "по возрастанию":
                date_flag = False
            else:
                date_flag = True
        filtered_transactions = sort_by_date(filtered_transactions, date_flag)

        filter_by_rub = input("Выводить только рублевые транзакции? Да/Нет ")
        if filter_by_rub.lower() == "да":
            rub_transactions = filter_by_currency(filtered_transactions, "RUB")
            filtered_transactions = list(rub_transactions)[:-1]

        fitered_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower
        if fitered_by_word == "да":
            word = input("Введите слово...")
            filtered_transactions = search_bank_operation(filtered_transactions, word)
        else:
            break

        print("Распечатываю итоговый список транзакций...")
        if len(filtered_transactions) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
            for transaction in filtered_transactions:
                mask_date = get_mask_account(transaction["date"])
                currency = transaction["operationAmount"]["currency"]["name"]
                if transaction["description"] == "Открытие вклада":
                    mask_card = get_mask_card_number(transaction["to"])
                else:
                    mask_card = get_mask_card_number(transaction["from"]) + " -> " + get_mask_account(transaction["to"])

                amount = transaction["operationAmount"]["amount"]
                print(f"""{mask_date} {transaction['description']} 
                        {mask_card}
                        Сумма: {round(float(amount))} {currency}""")


if __name__ == "__main__":
    main_menu()