from typing import List, Dict, Any, Generator

# Список транзакций (скопирован из вашего сообщения)
transaction = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 125485568,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "EUR", "code": "EUR"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2020-09-27T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "RUB", "code": "RUB"}
        },
        "description": "Перевод с карты на карту",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 45851235541258454215",
        "to": "Счет 78451541500054545054"
    }
]

# Функция фильтрации
def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> filter:

    """
    Функция для фильтрации транзакций по типу валюты
    """

    return filter(lambda t: t["operationAmount"]["currency"]["code"] == currency_code, transactions)

# Генератор описаний
def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Функция для вывода всех описаний транзакций
    """
    for trans in transactions:
        yield trans["description"]

# Проверка вывода фильтрации по типу валюты
if __name__ == "__main__":

   transaction_user = filter_by_currency(transaction, "USD")

   print("Сортировка по типу валюты:")
   for tran in transaction_user:
        print(tran)

# Проверка вывода описания транзакций
if __name__ == "__main__":

    descriptions = transaction_descriptions(transaction)

    print("Описания транзакций:")
    for desc in descriptions:
        print(desc)

def card_number_generator(start: int, end: int):
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        # Преобразуем число в строку и дополняем нулями слева до 16 знаков
        num_str = f"{number:016d}"
        # Форматируем в виде XXXX XXXX XXXX XXXX
        formatted_card_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield formatted_card_number

# Проверка вывода генератора номеров карт
for card_number in card_number_generator(1, 5):
    print(card_number)