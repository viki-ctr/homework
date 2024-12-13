import os
from functools import wraps
from time import sleep, time
from typing import AnyStr


def log(filename: str):
    """Декоратор, который автоматически логирует начало и конец выполнения функции, ее результаты/возникшие ошибки"""

    if filename and isinstance(filename, str):
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def decorator(func):
        @wraps(func)
        def wrapper(*args: tuple[AnyStr], **kwargs: dict[str, AnyStr]):
            try:
                time_1 = time()
                time_1_round = round(time_1, 1)
                result = func(*args, **kwargs)
                time_2 = time()
                time_2_round = round(time_2, 1)

                log_message = (
                    f"{func.__name__} ok. \n"
                    f"Start time: {time_1_round}. \n"
                    f"End time: {time_2_round}.\n"
                    f"Result: {result}\n"
                )
                if filename and filename.endswith(".txt"):
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)

                return result

            except Exception as e:
                error_message = (
                    f"{func.__name__} ERROR: {e.__class__.__name__}. \n" f"Inputs: args={args}, kwargs={kwargs}\n"
                )

                if filename and filename.endswith(".txt"):
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message)
                else:
                    print(error_message)

                raise

        return wrapper

    return decorator


@log(filename="log/mylog.txt")
def my_function(x, y):
    sleep(5)
    return x + y


my_function(1, 2)
