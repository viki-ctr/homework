import json
import logging
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_log = os.path.join(base_dir, "..", "logs", "util.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=file_path_log,
    encoding="utf-8",
    filemode="w",
)


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_json = os.path.join(base_dir, "..", "data", "operations.json")


def transaction(file=file_path_json):
    """Функция, принимающая путь до JSON-файла и возвращающая список словарей или пустой список"""
    with open(file, "r", encoding="UTF-8") as f:
        try:
            logging.info("Преобразуем файл формата JSON в объект Python")
            transactions_list = json.load(f)

            if len(transactions_list) == 0:
                logging.info("Файл пустой")
                return []

            else:
                logging.info("Файл в формате списка")
                return transactions_list

        except json.JSONDecodeError as ex:
            logging.error(f"Произошла ошибка {ex}", exc_info=True)
            return []


# data = transaction(file=file_path_json)
# print(data)
