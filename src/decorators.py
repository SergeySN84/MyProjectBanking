from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = open(filename, 'a') if filename else None
            try:
                # Логирование начала выполнения
                start_msg = (f"Выполнение функции {func.__name__} "
                             f"с аргументами args={args}, kwargs={kwargs}\n")
                if filename:
                    with open(filename, 'a') as f:
                        f.write(start_msg)
                else:
                    print(start_msg, end='')

                # Выполнение функции
                result = func(*args, **kwargs)

                # Логирование успешного завершения
                success_msg = (f"Функция {func.__name__} "
                               f"успешно завершена. Результат: {result}\n")
                if filename:
                    with open(filename, 'a') as f:
                        f.write(success_msg)
                else:
                    print(success_msg)
                return result
            except Exception as e:
                # Логирование ошибки
                error_msg = (f"Ошибка в функции {func.__name__}:"
                             f" {type(e).__name__}, "
                             f"Аргументы: args={args}, kwargs={kwargs}\n")
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_msg)
                else:
                    print(error_msg)
                raise  # Пробрасываем исключение дальше
            finally:
                if logger:
                    logger.close()

        return wrapper

    return decorator


@log()
def add(a, b):
    return a + b


add(3, 5)
