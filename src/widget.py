from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(num_acc_card: str) -> str | None:
    """Функция маскировки счета и карты"""
    try:
        if len(num_acc_card.split()[-1]) == 16:
            new_num = get_mask_card_number(num_acc_card.split()[-1])
            result = f"{num_acc_card[:-16]}{new_num}"
            return result
        elif len(num_acc_card.split()[-1]) == 20:
            new_num_acc = get_mask_account(num_acc_card.split()[-1])
            results = f"{num_acc_card[:-20]}{new_num_acc}"
            return results
    except IndexError:
        return None


def get_date(date_: str) -> str | None:
    """Функция вывода времени"""
    result_date = f"{date_[8:10]}.{date_[5:7]}.{date_[0:4]}"
    return result_date
