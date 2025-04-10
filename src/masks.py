def get_mask_card_number (card_number: str) -> str:
    """Функция скрывает маской номер карты"""

    return f"{str (card_number) [:4]} {str (card_number) [4:6]}** **** {str (card_number) [12:]}"


def get_mask_account (mask_account: str) -> str:
    """Функция скрывает номер банковского счета"""

    return f"**{str (mask_account) [-4:]}"
