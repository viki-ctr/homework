import pandas as pd
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_csv = os.path.join(base_dir, "..", "transactions.csv")

def get_csv_transactions(csv_doc=file_path_csv) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    with open(csv_doc, encoding='utf-8') as file:
        transaction_from_csv = pd.read_csv(file, delimiter=";")
        return transaction_from_csv.to_dict(orient="records")


print(get_csv_transactions())


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_excel = os.path.join(base_dir, "..", "transactions_excel.xlsx")

def get_excel_transactions(xlsx_doc=file_path_excel) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    transactions = pd.read_excel(file_path_excel)
    return transactions.to_dict(orient='records')


# print(get_excel_transactions())