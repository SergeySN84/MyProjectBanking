from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime
from typing import Optional


def mask_account_card(account_card: str) -> Optional[str]:
    """
    Функция для маскировки номера карты/счета.
    Используются ранее написанные функции из модуля masks.
    """
    account_card_list = account_card.split()

    if "Счет" in account_card_list:
        return f"{get_mask_account(account_card_list[1])}"

    if "MasterCard" in account_card_list or "Maestro" in account_card_list:
        card_type = account_card_list[0]
        card_number = account_card_list[1]
        return f"{card_type} {get_mask_card_number(card_number)}"

    if "Visa" in account_card_list:
        number_for_mask = []
        name_for_mask = []
        for item in account_card_list:
            if item.isdigit():
                number_for_mask.append(item)
            else:
                name_for_mask.append(item)

        str_number_card = "".join(number_for_mask)
        name_part = f"{name_for_mask[0]} {name_for_mask[1]}"
        masked_number = get_mask_card_number(str_number_card)

        return f"{name_part} {masked_number}"

    return None


def get_data(data: str) -> str:

    """Функция для корректного отображения даты"""

    date_obj = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


"""Вводим данные для проверки работы функцияй"""

print(get_data("2024-03-11T02:26:18.671407"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
