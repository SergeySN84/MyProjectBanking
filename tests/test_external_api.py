import pytest
import requests
from unittest.mock import patch, Mock
from src.external_api import get_currency_rate, CurrencyConversionError


# Тест 1: Успешный запрос
@patch("requests.get")
def test_get_currency_rate_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        "result": 80.5
    }
    mock_get.return_value = mock_response

    rate = get_currency_rate("USD", "RUB")
    assert rate == 80.5


# Тест 2: Ошибка 400 от API
@patch("requests.get")
def test_get_currency_rate_bad_request(mock_get):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
    mock_get.return_value = mock_response

    with pytest.raises(CurrencyConversionError):
        get_currency_rate("USD", "RUB")


# Тест 3: Ошибка при парсинге JSON
@patch("requests.get")
def test_get_currency_rate_json_decode_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("JSON decode error")
    mock_get.return_value = mock_response

    with pytest.raises(CurrencyConversionError):
        get_currency_rate("USD", "RUB")


# Тест 4: API вернул success=False
@patch("requests.get")
def test_get_currency_rate_api_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": False,
        "message": "invalid currency"
    }
    mock_get.return_value = mock_response

    with pytest.raises(CurrencyConversionError):
        get_currency_rate("XYZ", "RUB")


# Тест 5: API не вернул поле result
@patch("requests.get")
def test_get_currency_rate_missing_result(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        # "result" отсутствует
    }
    mock_get.return_value = mock_response

    with pytest.raises(CurrencyConversionError):
        get_currency_rate("USD", "RUB")
