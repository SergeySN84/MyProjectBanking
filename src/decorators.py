from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования вызовов функций: успешного завершения или ошибки.

    Аргументы:
        filename (str, optional): Имя файла, в который будут записываться логи.
                                  Если не указано, логи выводятся в консоль.
    """

    def decorator(func):
        """
        Внутренний декоратор, оборачивающий целевую функцию.

        Аргументы:
            func (function): Декорируемая функция.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Обёртка вокруг функции, добавляющая логирование.

            Аргументы:
                *args: Позиционные аргументы целевой функции.
                **kwargs: Именованные аргументы целевой функции.

            Возвращает:
                Результат выполнения целевой функции.

            Исключения:
                Перебрасывает любое исключение, возникшее
                при выполнении функции,
                после записи сообщения об ошибке в лог.
            """
            try:
                result = func(*args, **kwargs)

                msg = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(msg)
                else:
                    print(msg, end='')

                return result

            except Exception as e:
                msg = (f"{func.__name__} error: {type(e).__name__}."
                       f" Inputs: {args}, {kwargs}\n")
                if filename:
                    with open(filename, 'a') as f:
                        f.write(msg)
                else:
                    print(msg, end='')

                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
