from finance_operations import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)
from src.utils import read_transactions_from_json
from src.filters import (
    filter_by_status,
    filter_by_currency,
    filter_by_date,
    filter_by_description,
    count_by_category,
)
from src.widget import display_transactions
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    """
    Главная функция программы для работы с банковскими транзакциями.
    Реализует интерфейс для загрузки данных из файлов (JSON, CSV, XLSX),
    фильтрации, сортировки и вывода информации о транзакциях.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ").strip()

    if choice == "1":
        transactions = read_transactions_from_json("../data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        transactions = read_transactions_from_csv("../data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = read_transactions_from_excel("../data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Фильтрация по статусу
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию "
            "(EXECUTED, CANCELED, PENDING): "
        ).strip().upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_status(transactions, status)
            print(f"Операции отфильтрованы по статусу '{status}'.")
            break
        else:
            print("Статус операции недоступен. Попробуйте снова.")

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order = input(
            "Отсортировать по возрастанию или по убыванию? (возрастанию/убыванию): "
        ).strip().lower()
        ascending = True if order == "возрастанию" else False
        transactions = filter_by_date(transactions, ascending)

    # Фильтрация по валюте
    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == "да":
        transactions = filter_by_currency(transactions, "RUB")

    # Фильтрация по описанию
    description_choice = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
    ).strip().lower()
    if description_choice == "да":
        search_string = input("Введите слово для поиска в описании: ").strip()
        transactions = filter_by_description(transactions, search_string)

    # Определение категорий
    categories = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]

    # Подсчет операций по категориям
    category_counts = count_by_category(transactions, categories)

    # Вывод результатов
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")
        display_transactions(transactions)

        # Вывод подсчета категорий
        print("\nСтатистика по категориям:")
        for category, count in category_counts.items():
            print(f"{category}: {count} операций")


if __name__ == "__main__":
    """
    Точка входа программы.
    Вызывает главную функцию `main` для запуска программы.
    """
    main()
