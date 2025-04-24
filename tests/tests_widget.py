import pytest
from src.widget import get_data, mask_account_card


# Тесты для функции mask_account_card
def test_mask_account():
    """
    Тестирование маскировки номера счета.
    """
    input_data = "Счет 12345678901234567890"
    expected_output = "**7890"
    assert mask_account_card(input_data) == expected_output

def test_mask_mastercard():
    """
    Тестирование маскировки номера карты MasterCard.
    """
    input_data = "MasterCard 5100000000000008"
    expected_output = "MasterCard 5100 00** **** 0008"
    assert mask_account_card(input_data) == expected_output

def test_mask_maestro():
    """
    Тестирование маскировки номера карты Maestro.
    """
    input_data = "Maestro 6759000000000016"
    expected_output = "Maestro 6759 00** **** 0016"
    assert mask_account_card(input_data) == expected_output

def test_mask_visa():
    """
    Тестирование маскировки номера карты Visa.
    """
    input_data = "Visa Classic 4500000000000000"
    expected_output = "Visa Classic 4500 00** **** 0000"
    assert mask_account_card(input_data) == expected_output

def test_invalid_input():
    """
    Тестирование обработки некорректного ввода.
    """
    input_data = "Invalid Input"
    assert mask_account_card(input_data) is None

def test_empty_input():
    """
    Тестирование обработки пустого ввода.
    """
    input_data = ""
    assert mask_account_card(input_data) is None

def test_get_data_valid_format():
    """
    Тестирование функции get_data с корректным форматом входных данных.
    """
    input_data = "2023-10-05T14:48:00.123456"
    expected_output = "05.10.2023"

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


def test_get_data_edge_cases():
    """
    Тестирование граничных случаев, таких как начало и конец года.
    """
    # Начало года
    input_data_1 = "2023-01-01T00:00:00.000000"
    expected_output_1 = "01.01.2023"

    # Конец года
    input_data_2 = "2023-12-31T23:59:59.999999"
    expected_output_2 = "31.12.2023"

    assert get_data(input_data_1) == expected_output_1
    assert get_data(input_data_2) == expected_output_2