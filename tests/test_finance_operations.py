import unittest
from unittest.mock import patch, mock_open
from src.finance_operations import read_transactions_from_csv, read_transactions_from_excel
import pandas as pd


class TestReadTransactionsFromCSV(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open,
           read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
                     "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
                     "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации")
    def test_read_transactions_from_csv(self, mock_file):
        """
        Тестирование чтения данных из CSV-файла.
        """
        file_path = "data/transactions.csv"
        transactions = read_transactions_from_csv(file_path)

        expected_output = [{
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }]
        self.assertEqual(transactions, expected_output)
        mock_file.assert_called_once_with(file_path, mode='r', encoding='utf-8')

    @patch('builtins.open', side_effect=FileNotFoundError("Файл не найден"))
    def test_read_transactions_from_csv_file_not_found(self, mock_file):
        """
        Тестирование обработки ошибки FileNotFoundError в read_transactions_from_csv.
        """
        file_path = "data/nonexistent.csv"
        transactions = read_transactions_from_csv(file_path)
        self.assertEqual(transactions, [])
        mock_file.assert_called_once_with(file_path, mode='r', encoding='utf-8')

class TestReadTransactionsFromExcel(unittest.TestCase):

    @patch('pandas.read_excel')
    def test_read_transactions_from_excel(self, mock_read_excel):
        """
        Тестирование чтения данных из Excel-файла.
        """
        mock_data = {
            'id': [3854837],
            'state': ['EXECUTED'],
            'date': ['2023-08-11T04:42:10Z'],
            'amount': [29981],
            'currency_name': ['Euro'],
            'currency_code': ['EUR'],
            'from': ['Счет 55984099228760844878'],
            'to': ['Счет 41457533849518487584'],
            'description': ['Перевод со счета на счет']
        }
        mock_df = pd.DataFrame(mock_data)
        mock_read_excel.return_value = mock_df

        file_path = "data/transactions_excel.xlsx"
        transactions = read_transactions_from_excel(file_path)

        expected_output = [{
            'id': 3854837,
            'state': 'EXECUTED',
            'date': '2023-08-11T04:42:10Z',
            'amount': 29981,
            'currency_name': 'Euro',
            'currency_code': 'EUR',
            'from': 'Счет 55984099228760844878',
            'to': 'Счет 41457533849518487584',
            'description': 'Перевод со счета на счет'
        }]
        self.assertEqual(transactions, expected_output)
        mock_read_excel.assert_called_once_with(file_path)

    @patch('pandas.read_excel', side_effect=FileNotFoundError("Файл не найден"))
    def test_read_transactions_from_excel_file_not_found(self, mock_read_excel):
        """
        Тестирование обработки ошибки FileNotFoundError в read_transactions_from_excel.
        """
        file_path = "data/nonexistent.xlsx"
        transactions = read_transactions_from_excel(file_path)
        self.assertEqual(transactions, [])
        mock_read_excel.assert_called_once_with(file_path)
