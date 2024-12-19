import os
from typing import Any

import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_csv = os.path.join(base_dir, "..", "data", "transactions.csv")


def get_csv_transactions(csv_doc=file_path_csv) -> list[dict[Any, Any]]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    try:
        with open(csv_doc, encoding="utf-8") as file:
            transaction_from_csv = pd.read_csv(file, delimiter=";")
            return transaction_from_csv.to_dict(orient="records")
    except FileNotFoundError:
        return []


print(get_csv_transactions())


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_excel = os.path.join(base_dir, "..", "data", "transactions_excel.xlsx")


def get_excel_transactions(xlsx_doc=file_path_excel) -> list[dict[Any, Any]]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    try:
        transactions = pd.read_excel(xlsx_doc)
        return transactions.to_dict(orient="records")
    except FileNotFoundError:
        return []


# print(get_excel_transactions())
