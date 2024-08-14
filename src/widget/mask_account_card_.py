from src.mask import mask_acc_num, mask_card_num

def mask_account_card(num_acc_card: str) -> str | None:
    """Функция маскировки счета и карты"""
    if len(num_acc_card.split()[-1]) == 16:
        new_num = mask_card_num(num_acc_card.split()[-1])
        result = f"{num_acc_card[:-16]}{new_num}"
        return result
    elif len(num_acc_card.split()[-1]) == 20:
        new_num_acc = mask_acc_num(num_acc_card.split()[-1])
        results = f"{num_acc_card[:-20]}{new_num_acc}"
        return results
    else:
        return None