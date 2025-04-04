def get_mask_card_number (card_number: int) -> str:
    """Функция скрывает маской номер карты"""

    return f"{str (card_number) [:4]} {str (card_number) [4:6]}** **** {str (card_number) [12:]}"

print (get_mask_card_number (2536874125985234))


def get_mask_account (mask_account: int) -> str:
    """Функция скрывает номер банковского счета"""

    return f"**{str (mask_account) [-4:]}"

print (get_mask_account (25415896574123520058))
