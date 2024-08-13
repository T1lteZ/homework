def get_mask_account(num_acc: str) -> str | None:
    """Функция маскировки номера счета"""
    if num_acc.isdigit() and len(num_acc) == 20:
        return f"** {num_acc[-4:]}"
    else:
        return None
