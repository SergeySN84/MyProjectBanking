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
            # Создаем объект reader для чтения CSV-файла
            reader = csv.reader(file, delimiter=';')

            # Пропускаем заголовки
            headers = next(reader)

            for row in reader:
                if not row or len(row) < 9:  # Пропускаем пустые или неполные строки
                    continue

                # Создаем словарь для транзакции
                transaction = {
                    'state': row[1],
                    'date': row[2],
                    'amount': (row[3]),
                    'currency_name': row[4],
                    'currency_code': row[5],
                    'from': row[6] if row[6] else None,
                    'to': row[7],
                    'description': row[8]
                }
                transactions.append(transaction)

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
        # Преобразование DataFrame в список словарей
        #transactions = df.to_dict(orient='records')
        transactions = []
        for _, row in df.iterrows():
            transaction = {
                'id': row.get('id'),
                'state': row.get('state'),
                'date': row.get('date'),
                'amount': row.get('amount', ''),  # Или другой ключ, например 'operationAmount.amount'
                'currency_name': row.get('currency_name', ''),  # Или другой ключ, например 'currency'
                'currency_code': row.get('currency_code'),
                'from': row.get('from'),
                'to': row.get('to'),
                'description': row.get('description')
            }
            transactions.append(transaction)

        return transactions
    except Exception as e:
        print(f"Произошла ошибка при чтении XLSX файла: {e}")
        return []


# Определение пути к папке data
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_root, "data")

# Пути к файлам
csv_file_path = os.path.join(data_dir, "transactions.csv")
excel_file_path = os.path.join(data_dir, "transactions_excel.xlsx")
# # Чтение транзакций из CSV файла
# csv_transactions = read_transactions_from_csv(csv_file_path)
# print("Транзакции из CSV:")
# for transaction in csv_transactions[:5]:  # Вывод первых 5 транзакций
#     print(transaction)

# # Чтение транзакций из Excel файла
# excel_transactions = read_transactions_from_excel(excel_file_path)
# print("\nТранзакции из Excel:")
# for transaction in excel_transactions[:5]:  # Вывод первых 5 транзакций
#     print(transaction)
