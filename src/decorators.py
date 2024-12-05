from functools import wraps
from time import sleep, time
from typing import AnyStr


def log(filename: str = None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции, ее результаты/возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args: tuple[AnyStr], **kwargs: dict[str, AnyStr]):
            try:
                time_1 = time()
                time_1_round = round(time_1, 1)
                result = func(*args, **kwargs)
                time_2 = time()
                time_2_round = round(time_2, 1)

                if filename == str and ".txt" in filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok. \nStart time: {time_1_round}. \nEnd time: {time_2_round}.")
                else:
                    print(f"{func.__name__} ok. \nStart time: {time_1_round}. \nEnd time: {time_2_round}.")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ERROR : {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} ERROR : {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


@log(filename="logs/mylog.txt")
def my_function(x, y):
    sleep(5)
    return x + y


my_function(1, 2)
