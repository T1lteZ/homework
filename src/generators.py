from tests.conftest import transactions


def filter_by_currency(transactions: list[dict], currency="USD") -> list[dict]:
    """Фильтр списка словарей транзакций"""
    if len(transactions) > 0:
        for transactions in transactions:
            if transactions["operationAmount"]["currency"]["name"] == currency:
                yield transactions
            else:
                continue
    elif len(transactions) == 0:
        try:
            yield "Нет транзакций"
        except StopIteration:
            return "Нет транзакций"
    elif transactions == "":
        try:
            yield "Нет транзакций"
        except StopIteration:
            return "Нет транзакций"


usd_transactions = filter_by_currency(transactions, "USD")


def transaction_descriptions(transactions: list[dict]) -> str:
    """Функция вывода категории транзакции"""
    if len(transactions) > 0:
        for description in transactions:
            yield description["description"]
    elif len(transactions) == 0:
        try:
            yield "Нет транзакций"
        except StopIteration:
            return "Нет транзакций"
    elif transactions == "":
        try:
            yield "Нет транзакций"
        except StopIteration:
            return "Нет транзакций"


descriptions = transaction_descriptions(transactions)


def card_number_generator(start, end):
    """Генератор номера карт"""
    for i in range(start, end + 1):
        card_num_gen = "0000000000000000"
        str_sum = card_num_gen + str(i)
        card_number = f"{str_sum[-16:-12]} {str_sum[-12:-8]} {str_sum[-8:-4]} {str_sum[-4:-1]}{str_sum[-1]}"
        yield card_number
