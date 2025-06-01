from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime
from typing import Optional


def mask_account_card(account_card: str) -> Optional[str]:
    """
    Функция для маскировки номера карты/счета.
    Используются ранее написанные функции из модуля masks.
    """
    if not account_card:
        return None

    # Разделяем строку на части
    account_card_list = account_card.split()

    # Если это счет
    if "Счет" in account_card_list:
        return f"{get_mask_account(account_card_list[-1])}"

    # Если это MasterCard или Maestro
    if "MasterCard" in account_card_list or "Maestro" in account_card_list:
        card_type = account_card_list[0]
        card_number = account_card_list[-1]
        return f"{card_type} {get_mask_card_number(card_number)}"

    # Если это Visa
    if "Visa" in account_card_list:
        number_for_mask = []
        name_for_mask = []
        for item in account_card_list:
            if item.isdigit():
                number_for_mask.append(item)
            else:
                name_for_mask.append(item)

        str_number_card = "".join(number_for_mask)
        name_part = " ".join(name_for_mask)
        masked_number = get_mask_card_number(str_number_card)

        return f"{name_part} {masked_number}"

    # Если формат неизвестен
    return None


def display_transactions(transactions):
    """
    Выводит информацию о транзакциях в читаемом формате.
    Поддерживает разные структуры данных (JSON, CSV, XLSX).
    """
    for transaction in transactions:
        # Определяем тип данных по наличию ключей
        if 'operationAmount' in transaction:  # JSON-структура
            raw_date = transaction.get('date', '')
            description = transaction.get('description', '')
            amount = transaction.get('operationAmount', {}).get('amount', '')
            currency = (transaction.get('operationAmount', {}).
                        get('currency', {}).get('code', ''))
            from_account = transaction.get('from', '')
            to_account = transaction.get('to', '')

        elif 'currency_code' in transaction:  # CSV/XLSX-структура
            raw_date = transaction.get('date', '')
            description = transaction.get('description', '')
            amount = transaction.get('amount', '')
            currency = transaction.get('currency_code', '')
            from_account = transaction.get('from', '')
            to_account = transaction.get('to', '')

        else:
            print("Неизвестная структура данных. Пропускаем транзакцию.")
            continue

        # Обработка даты
        if raw_date.endswith('Z'):
            raw_date = raw_date[:-1]
        if '.' in raw_date:
            raw_date = raw_date.split('.')[0]  # Обрезаем миллисекунды
        try:
            date_obj = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S")
        except ValueError as e:
            print(f"Ошибка при обработке даты '{raw_date}': {e}")
            continue

        formatted_date = date_obj.strftime("%d.%m.%Y")

        # Вывод информации
        print(f"{formatted_date} {description}")
        if from_account:
            print(f"{from_account}")
        print(f"{to_account}")
        print(f"Сумма: {amount} {currency}\n")
