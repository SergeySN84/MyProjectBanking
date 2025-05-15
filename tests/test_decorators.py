import os
import pytest
from src.decorators import log

LOG_FILE = "mylog.txt"


@pytest.fixture(autouse=True)
def cleanup_log_file():
    """Очищает лог-файл до и после каждого теста."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    yield
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)


def test_successful_execution_logs_to_console(capsys):
    """Проверяет, что успешный вызов записывается в консоль."""

    @log()
    def say_hello(name):
        return f"Hello, {name}!"

    say_hello("Alice")

    captured = capsys.readouterr()
    assert captured.out == "say_hello ok\n"
    assert captured.err == ""


def test_error_execution_logs_to_console(capsys):
    """Проверяет, что исключение логируется в консоль."""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert ("divide error: ZeroDivisionError."
            " Inputs: (10, 0), {}") in captured.out
    assert captured.err == ""


def test_successful_execution_logs_to_file():
    """Проверяет, что успешный вызов записывается в файл."""

    @log(filename=LOG_FILE)
    def multiply(a, b):
        return a * b

    multiply(3, 4)

    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'r') as f:
        content = f.read()
    assert content == "multiply ok\n"


def test_error_execution_logs_to_file():
    """Проверяет, что исключение записывается в файл."""

    @log(filename=LOG_FILE)
    def power(a, b):
        return a ** b

    with pytest.raises(TypeError):
        power("two", 2)

    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'r') as f:
        content = f.read()
    assert ("power error: TypeError."
            " Inputs: ('two', 2), {}") in content
