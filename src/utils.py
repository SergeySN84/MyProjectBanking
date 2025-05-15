import os
import json
import logging


current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
log_file_path = os.path.join(log_dir, 'utils.log')
file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s '
                                   '- %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> list:
    """
    Читает данные о финансовых транзакциях из JSON-файла.
    """
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        logger.info("Проверяем, существует ли файл")
        logger.error(f"Файл не найден: {file_path}")
        return []

    # Читаем содержимое файла
    try:
        logger.info("Читаем содержимое файла")
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        logger.error(f"Файл содержит некорректный JSON: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        return []

    # Проверяем, является ли содержимое списком
    if not isinstance(data, list):
        logger.info("Проверяем, является ли содержимое списком")
        logger.error(f"Содержимое файла не является списком: {file_path}")
        return []

    # Проверяем, что каждый элемент списка - словарь
    logger.info("Проверяем, что каждый элемент списка - словарь")
    for item in data:
        if not isinstance(item, dict):
            logger.error(f"Элементы списка должны быть словарями: {file_path}")
            return []

    return data


# Определяем путь к файлу
file_path_outer = os.path.abspath(os.path.join('..',
                                               'data', 'operations.json'))

# Проверяем существование файла
if not os.path.exists(file_path_outer):
    logger.error(f"Файл не существует по пути: {file_path_outer}")
else:
    logger.info(f"Файл найден: {file_path_outer}")

# Чтение данных
transactions = read_transactions(file_path_outer)

# Вывод результата
print("Транзакции:", transactions)
