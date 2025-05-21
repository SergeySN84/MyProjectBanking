import csv
import pandas as pd
import os

def read_transactions_from_csv(file_path: str) -> list:
    """
    Считывает финансовые операции из CSV файла и возвращает список словарей с транзакциями.

    :param file_path: Путь к CSV файлу
    :return: Список словарей с транзакциями
    """
    transactions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении CSV файла: {e}")
    return transactions


def read_transactions_from_excel(file_path: str) -> list:
    """
    Считывает финансовые операции из Excel файла и возвращает список словарей с транзакциями.

    """
    transactions = []
    try:
        # Чтение данных из Excel файла с помощью pandas
        df = pd.read_excel(file_path)
        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении Excel файла: {e}")
    return transactions


# Определение пути к папке data
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Корень проекта
data_dir = os.path.join(project_root, "data")  # Папка data

# Пути к файлам
csv_file_path = os.path.join(data_dir, "transactions.csv")
excel_file_path = os.path.join(data_dir, "transactions_excel.xlsx")
# Чтение транзакций из CSV файла
csv_transactions = read_transactions_from_csv(csv_file_path)
print("Транзакции из CSV:")
for transaction in csv_transactions[:5]:  # Вывод первых 5 транзакций
    print(transaction)

# Чтение транзакций из Excel файла
excel_transactions = read_transactions_from_excel(excel_file_path)
print("\nТранзакции из Excel:")
for transaction in excel_transactions[:5]:  # Вывод первых 5 транзакций
    print(transaction)