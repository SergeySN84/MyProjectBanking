import csv
import pandas as pd
import os


def read_transactions_from_csv(file_path):
    """
    Читает данные о транзакциях из CSV-файла.
    Возвращает список словарей.
    """
    transactions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                # Создаем словарь для транзакции
                transaction = {
                    'state': row['state'],
                    'date': row['date'],
                    'amount': row['amount'],
                    'currency_name': row['currency_name'],
                    'currency_code': row['currency_code'],
                    'from': row['from'] if row['from'] else None,
                    'to': row['to'],
                    'description': row['description']
                }
                transactions.append(transaction)

    except FileNotFoundError:
        print("Произошла ошибка при чтении CSV файла: Файл не найден")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении CSV файла: {e}")

    return transactions


def read_transactions_from_excel(file_path: str) -> list:
    """
    Считывает финансовые операции из Excel файла и возвращает
    список словарей с транзакциями.

    """
    try:
        # Чтение данных из Excel файла с помощью pandas
        df = pd.read_excel(file_path)

        transactions = []
        for _, row in df.iterrows():
            transaction = {
                'id': row.get('id'),
                'state': row.get('state'),
                'date': row.get('date'),
                'amount': row.get('amount', ''),
                'currency_name': row.get('currency_name', ''),
                'currency_code': row.get('currency_code'),
                'from': row.get('from'),
                'to': row.get('to'),
                'description': row.get('description')
            }
            transactions.append(transaction)

        return transactions
    except FileNotFoundError:
        print("Произошла ошибка при чтении XLSX файла: Файл не найден")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении XLSX файла: {e}")
        return []


# Определение пути к папке data
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_root, "data")

# Пути к файлам
csv_file_path = os.path.join(data_dir, "transactions.csv")
excel_file_path = os.path.join(data_dir, "transactions_excel.xlsx")
