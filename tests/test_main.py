import unittest
import os
from src.main import main# Предполагается, что main находится в src/main.py
from unittest.mock import patch

class TestMainWithoutMocks(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.original_dir = os.getcwd()  # Сохраняем текущую рабочую директорию
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Переходим в директорию с тестами

    def tearDown(self):
        """Очистка после каждого теста."""
        os.chdir(self.original_dir)  # Возвращаемся в исходную директорию

    def test_main_json(self):
        """Тест основного потока программы с JSON-файлом."""
        with patch('builtins.input', side_effect=["1", "EXECUTED", "нет", "нет", "нет"]):
            main()

    def test_main_csv(self):
        """Тест основного потока программы с CSV-файлом."""
        with patch('builtins.input', side_effect=["2", "EXECUTED", "нет", "нет", "нет"]):
            main()

    def test_main_excel(self):
        """Тест основного потока программы с XLSX-файлом."""
        with patch('builtins.input', side_effect=["3", "EXECUTED", "нет", "нет", "нет"]):
            main()

    def test_main_invalid_choice(self):
        """Тест завершения программы при неверном выборе пункта меню."""
        with patch('builtins.input', side_effect=["4"]):
            main()


if __name__ == "__main__":
    unittest.main()