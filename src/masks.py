import logging
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
log_file_path = os.path.join(log_dir, 'masks.log')
file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s '
                                   '- %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция скрывает маской номер карты"""
    logger.info("Скрываем маской номер карты")
    return (
        f"{str(card_number)[:4]} "
        f"{str(card_number)[4:6]}** **** "
        f"{str(card_number)[12:]}"
    )


def get_mask_account(mask_account: str) -> str:
    """Функция скрывает номер банковского счета"""
    try:
        if not mask_account.isdigit() or len(mask_account) < 4:
            raise ValueError("Номер счета должен содержать минимум 4 цифры")

        logger.info(f"Скрываем номер банковского счета: {mask_account}")
        return f"**{mask_account[-4:]}"

    except Exception as e:
        logger.error(f"Ошибка при маскировке счета: {e}", exc_info=True)
        return ""


if __name__ == "__main__":
    get_mask_card_number("1234567890123456")
    get_mask_account("12345678901234567890")
