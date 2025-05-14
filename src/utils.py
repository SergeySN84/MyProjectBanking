import os
import json


def read_transactions(file_path: str) -> list:
    """
    Читает данные о финансовых транзакциях из JSON-файла.
    """
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return []

    # Читаем содержимое файла
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Файл содержит некорректный JSON: {file_path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    # Проверяем, является ли содержимое списком
    if not isinstance(data, list):
        print(f"Содержимое файла не является списком: {file_path}")
        return []

    # Проверяем, что каждый элемент списка - словарь
    for item in data:
        if not isinstance(item, dict):
            print(f"Элементы списка должны быть словарями: {file_path}")
            return []

    return data


# Определяем путь к файлу
file_path_outer = os.path.abspath(os.path.join('..',
                                               'data', 'operations.json'))

# Проверяем существование файла
if not os.path.exists(file_path_outer):
    print(f"Файл не существует по пути: {file_path_outer}")
else:
    print(f"Файл найден: {file_path_outer}")

# Чтение данных
transactions = read_transactions(file_path_outer)

# Вывод результата
print("Транзакции:", transactions)
