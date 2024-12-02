from functools import wraps
from time import time
from typing import AnyStr


def log(filename: str = None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции, ее результаты/возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args: tuple[AnyStr], **kwargs: dict[str, AnyStr]):
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                if filename == str and ".txt" in filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok. \nStart time: {time_1}. \nEnd time: {time_2}")
                else:
                    print(f"{func.__name__} ok. \nStart time: {time_1}. \nEnd time: {time_2}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ERROR : {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} ERROR : {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")

        return wrapper

    return decorator


@log(filename="logs/mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
