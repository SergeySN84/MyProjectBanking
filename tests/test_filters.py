import unittest
from src.filters import (
    filter_by_status,
    filter_by_currency,
    filter_by_date,
    filter_by_description,
    count_by_category,
)


class TestFilters(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных."""
        self.transactions = [
            {"id": 1, "state": "EXECUTED", "date":
                "2023-09-05T11:30:32Z", "operationAmount":
                {"currency": {"code": "RUB"}},
             "description": "Перевод организации"},
            {"id": 2, "state": "CANCELED", "date":
                "2023-08-01T10:00:00Z", "operationAmount":
                {"currency": {"code": "USD"}},
             "description": "Открытие вклада"},
            {"id": 3, "state": "EXECUTED", "date":
                "2023-07-15T12:45:00Z", "operationAmount":
                {"currency": {"code": "RUB"}},
             "description": "Перевод со счета на счет"},
            {"id": 4, "state": "EXECUTED", "date":
                "2023-06-01T09:20:00Z", "operationAmount":
                {"currency": {"code": "EUR"}},
             "description": "Перевод с карты на карту"},
        ]

    def test_filter_by_status(self):
        """Тест фильтрации по статусу."""
        result = filter_by_status(self.transactions, "EXECUTED")
        self.assertEqual(len(result), 3)
        self.assertTrue(all(t["state"] == "EXECUTED" for t in result))

    def test_filter_by_currency(self):
        """Тест фильтрации по валюте."""
        result = filter_by_currency(self.transactions, "RUB")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(t["operationAmount"]["currency"]["code"] ==
                            "RUB" for t in result))

    def test_filter_by_date(self):
        """Тест сортировки по дате."""
        result_asc = filter_by_date(self.transactions, ascending=True)
        self.assertEqual([t["id"] for t in result_asc], [4, 3, 2, 1])

        result_desc = filter_by_date(self.transactions, ascending=False)
        self.assertEqual([t["id"] for t in result_desc], [1, 2, 3, 4])

    def test_filter_by_description(self):
        """Тест фильтрации по описанию."""
        result = filter_by_description(self.transactions, "перевод")
        self.assertEqual(len(result), 3)
        self.assertTrue(all("перевод" in t["description"]
                            .lower() for t in result))

    def test_count_by_category(self):
        """Тест подсчета категорий."""
        categories = ["Перевод организации", "Открытие вклада"]
        result = count_by_category(self.transactions, categories)
        self.assertEqual(result, {"Перевод организации": 1,
                                  "Открытие вклада": 1})


if __name__ == "__main__":
    unittest.main()
