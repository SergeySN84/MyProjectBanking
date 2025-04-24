import pytest
from src.widget import get_data, mask_account_card

# Фикстура для тестовых данных маскировки карт и счетов
@pytest.fixture
def masking_test_data():
    return [
        ("Счет 12345678901234567890", "**7890"),
        ("MasterCard 5100000000000008", "MasterCard 5100 00** **** 0008"),
        ("Maestro 6759000000000016", "Maestro 6759 00** **** 0016"),
        ("Visa Classic 4500000000000000", "Visa Classic 4500 00** **** 0000"),
        ("Invalid Input", None),
        ("", None)
    ]

# Тесты для функции mask_account_card
@pytest.mark.parametrize("input_data, expected_output", [
    ("Счет 12345678901234567890", "**7890"),
    ("MasterCard 5100000000000008", "MasterCard 5100 00** **** 0008"),
    ("Maestro 6759000000000016", "Maestro 6759 00** **** 0016"),
    ("Visa Classic 4500000000000000", "Visa Classic 4500 00** **** 0000"),
    ("Invalid Input", None),
    ("", None)
])
def test_mask_account_card(input_data, expected_output):
    """
    Параметризованный тест для функции mask_account_card.
    """
    assert mask_account_card(input_data) == expected_output

# Фикстура для тестовых данных функции get_data
@pytest.fixture
def date_test_data():
    return [
        ("2023-10-05T14:48:00.123456", "05.10.2023"),
        ("2023-01-01T00:00:00.000000", "01.01.2023"),
        ("2023-12-31T23:59:59.999999", "31.12.2023")
    ]

# Тесты для функции get_data
@pytest.mark.parametrize("input_data, expected_output", [
    ("2023-10-05T14:48:00.123456", "05.10.2023"),
    ("2023-01-01T00:00:00.000000", "01.01.2023"),
    ("2023-12-31T23:59:59.999999", "31.12.2023")
])
def test_get_data_valid_format(input_data, expected_output):
    """
    Параметризованный тест для функции get_data с корректным форматом входных данных.
    """
    result = get_data(input_data)
    assert result == expected_output, f"Ожидалось {expected_output}, но получено {result}"


def test_get_data_invalid_format():
    """
    Тестирование функции get_data с некорректным форматом входных данных.
    Проверяем, что возникает ValueError при неправильном формате.
    """
    invalid_input = "2023/10/05 14:48:00"
    with pytest.raises(ValueError):
        get_data(invalid_input)