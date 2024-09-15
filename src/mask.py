import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


file_path_rel = os.path.join(current_dir, "../logs/masks.log")
file_path_abs = os.path.abspath(file_path_rel)


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(file_path_abs, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str | None:
    """Функция маскировки номера карты"""
    if card_num.isdigit() and len(card_num) == 16:
        logger.info("Правильный формат номера карты")
        return f"{card_num[:4]} {card_num[4: 6]}{"*" * 2} {"*" * 4} {card_num[12:]}"
    else:
        logger.info("Неверный формат номера карты")
        return None


def get_mask_account(num_acc: str) -> str | None:
    """Функция маскировки номера счета"""
    if num_acc.isdigit() and len(num_acc) == 20:
        logger.info("Правильный формат номера счета")
        return f"**{num_acc[-4:]}"
    else:
        logger.info("Неверный формат номера счета")
        return None
