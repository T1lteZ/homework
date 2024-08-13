def get_mask_card_number(card_num: int) -> str | None:
    """Функция маскировки номера карты"""
    if card_num.isdigit() and len(card_num) == 16:
        return f"{card_num[:5]} {card_num[4: 6]}{"*" * 2} {"*" * 4} {card_num[12:]}"
    else:
        return None