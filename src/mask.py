def get_mask_card_number(card_num: int) -> str | None:
    """Функция маскировки номера карты"""
    if card_num.isdigit() and len(card_num) == 16:
        return f"{card_num[:5]} {card_num[4: 6]}{"*" * 2} {"*" * 4} {card_num[12:]}"
    else:
        return None


def get_mask_account(num_acc: str) -> str | None:
    """Функция маскировки номера счета"""
    if num_acc.isdigit() and len(num_acc) == 20:
        return f"** {num_acc[-4:]}"
    else:
        return None