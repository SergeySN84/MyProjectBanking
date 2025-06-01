import re
from collections import Counter


def filter_by_description(transactions, search_string):
    """
    Фильтрует транзакции по подстроке в поле 'description'.
    Использует регулярные выражения для поиска.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [
        transaction for transaction in transactions
        if pattern.search(transaction.get('description', ''))
    ]


def count_by_category(transactions: list, categories: list) -> dict:
    """
    Подсчитывает количество операций в каждой категории.

    """
    # Извлекаем описания всех транзакций
    descriptions = [
        transaction.get('description', '').strip()
        for transaction in transactions
        if transaction.get('description', '').strip() in categories
    ]

    # Используем Counter для подсчета количества операций по категориям
    category_counts = Counter(descriptions)

    # Преобразуем Counter в обычный словарь для совместимости
    return dict(category_counts)


def filter_by_status(transactions, status):
    """
    Фильтрует транзакции по статусу.
    """
    return [t for t in transactions if str(t.get('state', '')).upper()
            == status]


def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по валюте.
    Поддерживает разные структуры данных.
    """
    filtered_transactions = []

    for transaction in transactions:
        # Проверяем структуру данных для JSON
        if 'operationAmount' in transaction:
            transaction_currency = (transaction.get('operationAmount', {})
                                    .get('currency', {}).get('code', ''))
        # Проверяем структуру данных для CSV
        elif 'currency_code' in transaction:
            transaction_currency = transaction.get('currency_code', '')
        else:
            continue  # Пропускаем транзакции с неизвестной структурой

        # Если валюта совпадает с запрошенной, добавляем транзакцию
        if transaction_currency == currency_code:
            filtered_transactions.append(transaction)

    return filtered_transactions


def filter_by_date(transactions, ascending=True):
    """
    Сортирует транзакции по дате.
    """
    return sorted(
        transactions,
        key=lambda t: t.get('date', ''),
        reverse=not ascending
    )
