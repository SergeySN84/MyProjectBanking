import unittest
from unittest.mock import patch, mock_open
from src.finance_operations import (read_transactions_from_csv,
                                    read_transactions_from_excel)


class TestFinanceOperations(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open,
           read_data="id,state,date,amount\n1,EXECUTED,2023-09-05,16210")
    def test_read_transactions_from_csv(self, mock_file):
        """
        Тестирование функции read_transactions_from_csv
        с использованием mock_open.
        """
        # Путь к файлу (фиктивный)
        file_path = "data/transactions.csv"

        # Вызов функции
        transactions = read_transactions_from_csv(file_path)

        # Проверка результата
        expected_output = [{'id': '1', 'state': 'EXECUTED',
                            'date': '2023-09-05', 'amount': '16210'}]
        self.assertEqual(transactions, expected_output)
        mock_file.assert_called_once_with(file_path,
                                          mode='r', encoding='utf-8')

    @patch('pandas.read_excel')
    def test_read_transactions_from_excel(self, mock_read_excel):
        """
        Тестирование функции read_transactions_from_excel
        с использованием patch.
        """

        mock_read_excel.return_value.to_dict.return_value = [
            {'id': 1, 'state': 'EXECUTED',
             'date': '2023-09-05', 'amount': 16210}
        ]

        # Путь к файлу (фиктивный)
        file_path = "data/transactions_excel.xlsx"

        # Вызов функции
        transactions = read_transactions_from_excel(file_path)

        # Проверка результата
        expected_output = [{'id': 1, 'state': 'EXECUTED',
                            'date': '2023-09-05', 'amount': 16210}]
        self.assertEqual(transactions, expected_output)
        mock_read_excel.assert_called_once_with(file_path)

    @patch('builtins.open',
           side_effect=FileNotFoundError("Файл не найден"))
    def test_read_transactions_from_csv_file_not_found(self, mock_file):
        """
        Тестирование обработки ошибки FileNotFoundError
        в read_transactions_from_csv.
        """
        # Путь к файлу (фиктивный)
        file_path = "data/nonexistent.csv"

        # Вызов функции
        transactions = read_transactions_from_csv(file_path)

        # Проверка результата
        self.assertEqual(transactions, [])
        mock_file.assert_called_once_with(file_path,
                                          mode='r', encoding='utf-8')

    @patch('pandas.read_excel',
           side_effect=FileNotFoundError("Файл не найден"))
    def test_read_transactions_from_excel_file_not_found(self,
                                                         mock_read_excel):
        """
        Тестирование обработки ошибки FileNotFoundError
        в read_transactions_from_excel.
        """
        # Путь к файлу (фиктивный)
        file_path = "data/nonexistent.xlsx"

        # Вызов функции
        transactions = read_transactions_from_excel(file_path)

        # Проверка результата
        self.assertEqual(transactions, [])
        mock_read_excel.assert_called_once_with(file_path)


if __name__ == '__main__':
    unittest.main()
