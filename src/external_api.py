import requests
from dotenv import load_dotenv
import os
from src.utils import read_transactions

class CurrencyConversionError(Exception):
    """Исключение для ошибок при конвертации валют."""
    pass


def get_currency_rate(base_currency: str, target_currency: str = "RUB") -> float:
    """
    Получает текущий курс валюты по отношению к целевой валюте (по умолчанию RUB).
    """

    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
    load_dotenv(env_path)
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API ключ не найден. Убедитесь, что файл .env содержит переменную API_KEY.")

    # Чистим значения от пробелов
    base_currency = base_currency.strip().upper()
    target_currency = target_currency.strip().upper()

    # Корректный URL без лишних пробелов
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": api_key}
    params = {
        "from": base_currency,
        "to": target_currency,
        "amount": 1
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Проверяем HTTP-ошибки
        data = response.json()

        if not data.get("success"):
            error_msg = data.get("message", "Неизвестная ошибка от API")
            raise CurrencyConversionError(f"Ошибка от API: {error_msg}")

        if "result" in data:
            return data["result"]
        else:
            raise CurrencyConversionError("Ответ API не содержит 'result'")
    except requests.exceptions.RequestException as e:
        raise CurrencyConversionError(f"Ошибка при запросе к API: {e}")
    except Exception as e:
        raise CurrencyConversionError(f"Неожиданная ошибка: {e}")


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму в рубли, если валюта отлична от RUB.
    """

    if currency == "RUB":
        return amount

    try:
        rate = get_currency_rate(currency)
        return amount * rate
    except CurrencyConversionError as e:
        print(f"[Предупреждение] Не удалось конвертировать {amount} {currency}: {e}")
        return float('nan')  # NaN — как индикатор ошибки, можно заменить на 0 или None


def get_transaction_amount_in_rub(transaction: dict) -> float:
    """
    Возвращает сумму транзакции в рублях.
    """

    if not isinstance(transaction, dict):
        raise TypeError("Транзакция должна быть словарем")

    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"].strip().upper()
    except KeyError as e:
        raise KeyError(f"Отсутствует обязательное поле в транзакции: {e}")
    except ValueError:
        raise ValueError("Сумма транзакции не является числом")

    # Конвертируем сумму в рубли
    rub_amount = convert_to_rub(amount, currency)
    return rub_amount


# Определяем путь к файлу
file_path_outer = os.path.abspath(os.path.join('..', 'data', 'operations.json'))

# Чтение данных
transactions_list = read_transactions(file_path_outer)

# Обработка всех транзакций
for single_transaction in transactions_list:
    try:
        rub_total = get_transaction_amount_in_rub(single_transaction)
        print(f"Сумма транзакции в рублях: {rub_total:.2f}")
    except CurrencyConversionError as conversion_error:
        print(f"Ошибка конвертации валюты: {conversion_error}")
    except ValueError as value_error:
        print(f"Некорректные данные в транзакции: {value_error}")
    except KeyError as key_error:
        print(f"Ошибка формата транзакции: {key_error}")