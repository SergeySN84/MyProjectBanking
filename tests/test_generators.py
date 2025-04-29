import pytest
from src.generators import (filter_by_currency, transaction_descriptions,
                            card_number_generator)

# Пример данных для тестирования
transactions = [
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


# Фикстура: исходные данные

@pytest.fixture
def sample_transactions():
    return transactions


# Тестирование: filter_by_currency

@pytest.mark.parametrize("currency_code, expected_count", [
    ("USD", 2),
    ("EUR", 1),
    ("RUB", 1),
    ("JPY", 0),
])
def test_filter_by_currency(sample_transactions, currency_code, expected_count):
    result = list(filter_by_currency(sample_transactions, currency_code))
    assert len(result) == expected_count
    for item in result:
        assert item["operationAmount"]["currency"]["code"] == currency_code

# Тест на пустой список
def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0


# Тестирование: transaction_descriptions

def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert descriptions == expected

# Тест на пустой список
def test_transaction_descriptions_empty_list():
    assert list(transaction_descriptions([])) == []

# Тест на отсутствие ключа "description"
def test_transaction_descriptions_missing_key():
    bad_data = [{}]
    with pytest.raises(KeyError):
        list(transaction_descriptions(bad_data))

# Тест на частично отсутствующие описания
def test_transaction_descriptions_partial_missing():
    mixed_data = [
        {"description": "Перевод 1"},
        {},  # нет description
        {"description": "Перевод 2"}
    ]
    with pytest.raises(KeyError):  # Если вы не обрабатываете такие случаи
        list(transaction_descriptions(mixed_data))


# Тестирование: card_number_generator

@pytest.mark.parametrize("start, stop, expected_result", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999999999999997, 9999999999999999, [
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ])
])
def test_card_number_generator(start, stop, expected_result):
    result = list(card_number_generator(start, stop))
    assert result == expected_result

# Тест на ValueError при некорректном диапазоне
def test_card_number_generator_invalid_start():
    with pytest.raises(ValueError):
        list(card_number_generator(-1, 1))

def test_card_number_generator_invalid_end():
    with pytest.raises(ValueError):
        list(card_number_generator(1, 10000000000000000))

# Тест на start > end
def test_card_number_generator_start_greater_end():
    result = list(card_number_generator(10, 1))
    assert result == []  # Пустой список, если start > end

# Тест на граничные значения
def test_card_number_generator_edge_values():
    result = list(card_number_generator(0, 0))
    assert result == ["0000 0000 0000 0000"]

def test_card_number_generator_max_value():
    result = list(card_number_generator(9999999999999999, 9999999999999999))
    assert result == ["9999 9999 9999 9999"]
