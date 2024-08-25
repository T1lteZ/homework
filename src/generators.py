def filter_by_currency(transactions: list[dict], currency="USD") -> list[dict]:
    if len(transactions) > 0:
        for transactions in transactions:
            if transactions["operationAmount"]["currency"]["name"] == currency:
                yield transactions
            else:
                continue
    elif len(transactions) == 0:
        return "Нет транзакций"
    elif transactions == "":
        return "Нет транзакций"


usd_transactions = filter_by_currency(transactions, currency)


def transaction_descriptions(transactions: list[dict]) -> str:
    if len(transactions) > 0:
        for description in transactions:
            yield description["description"]
    elif len(transactions) == 0:
        return "Нет транзакций"
    elif transactions == "":
        return "Нет транзакций"


descriptions = transaction_descriptions(transactions)


def card_number_generator(start, end):
    for i in range(start, end + 1):
        card_num_gen = "0000000000000000"
        str_sum = card_num_gen + str(i)
        card_number = f"{str_sum[-16:-12]} {str_sum[-12:-8]} {str_sum[-8:-4]} {str_sum[-4:-1]}{str_sum[-1]}"
        yield card_number

