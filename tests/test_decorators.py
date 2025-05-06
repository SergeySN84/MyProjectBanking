import pytest

# Импортируем декоратор и тестовую функцию
from src.decorators import log


# Тест для проверки логирования в консоль
def test_log_to_console(capsys):
    @log()
    def test_func(a, b):
        return a + b

    test_func(2, 3)

    captured = capsys.readouterr()
    assert ("Выполнение функции test_func с аргументами args=(2, 3),"
            " kwargs={}") in captured.out
    assert ("Функция test_func успешно завершена. "
            "Результат: 5") in captured.out


# Тест для проверки логирования в файл
def test_log_to_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    multiply(4, 5)

    content = log_file.read_text()
    assert ("Выполнение функции multiply с аргументами args=(4, 5),"
            " kwargs={}") in content
    assert "Функция multiply успешно завершена. Результат: 20" in content


# Тест для проверки обработки исключений
def test_error_handling(capsys):
    @log()
    def faulty_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        faulty_func()

    captured = capsys.readouterr()
    assert ("Выполнение функции faulty_func с аргументами args=(),"
            " kwargs={}") in captured.out
    assert ("Ошибка в функции faulty_func: ValueError,"
            " Аргументы: args=(), kwargs={}") in captured.out


# Тест для проверки сохранения метаданных функции
def test_metadata_preservation():
    @log()
    def original_func():
        """Original docstring"""
        pass

    assert original_func.__name__ == "original_func"
    assert original_func.__doc__ == "Original docstring"


# Тест для проверки логирования именованных аргументов
def test_keyword_arguments_logging(capsys):
    @log()
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    greet(name="Alice", greeting="Hi")

    captured = capsys.readouterr()
    assert "args=()" in captured.out
    assert "kwargs={'name': 'Alice', 'greeting': 'Hi'}" in captured.out
    assert "Результат: Hi, Alice!" in captured.out


# Тест для проверки работы с разными типами аргументов
def test_complex_arguments_logging(capsys):
    @log()
    def process_data(data: list, flag: bool = False):
        return len(data) if flag else sum(data)

    test_data = [1, 2, 3]
    process_data(test_data, flag=True)

    captured = capsys.readouterr()
    assert "args=([1, 2, 3],)" in captured.out
    assert "kwargs={'flag': True}" in captured.out
    assert "Результат: 3" in captured.out
