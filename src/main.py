import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, search_operations, sort_by_date
from src.reading_transactions import get_csv_transactions, get_excel_transactions
from src.utils import transaction
from src.widget import get_date, mask_account_card

base_dir = os.path.dirname(os.path.abspath(__file__))
PATH_TO_FILE_JSON = os.path.join(base_dir, "..", "data", "operations.json")
PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def main():
    """Основная логика программы"""

    print(
        """Программа: Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
          """
    )
    start_menu = input("Пользователь: ")

    if start_menu == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = transaction(PATH_TO_FILE_JSON)
    elif start_menu == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = get_csv_transactions(PATH_TO_FILE_CSV)
    elif start_menu == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = get_excel_transactions(PATH_TO_FILE_EXCEL)
    else:
        print("Некорректный ввод")
        return

    print(
        """Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
           Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )

    operation_statues = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        try:
            user_statues = input("Пользователь: ").upper()
            statues_str = str(user_statues)
            if statues_str not in operation_statues:
                print(
                    """Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
               Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
                )
            else:
                break
        except (ValueError, TypeError):
            print("Введены некорретные данные")

    filtered_list = filter_by_state(transactions, state=user_statues)
    print(f"Программа: Операции отфильтрованы по статусу {user_statues}")

    print("Программа: Отсортировать операции по дате? Да/Нет")
    sorted_operations = input("Пользователь: ")
    if sorted_operations.lower() == "да":
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        while True:
            sorted_reverse = input("Пользователь: ")
            if sorted_reverse.lower() == "по убыванию":
                sort_date = sort_by_date(filtered_list)
                break
            elif sorted_reverse.lower() == "по возрастанию":
                sort_date = sort_by_date(filtered_list, reverse=False)
                break
            else:
                print("Выберите метод сортировки")
    else:
        sort_date = filtered_list

    print("Программа: Выводить только рублевые тразакции? Да/Нет")
    currency_operation = input("Пользователь: ")
    if currency_operation.lower() == "да":
        currency_transaction = filter_by_currency(sort_date, currency="RUB")
    else:
        currency_transaction = sort_date

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_answer = input("Пользователь: ")
    if user_answer.lower() == "да":
        word_filter = input("Введите слово: ")
        word_filter_transaction = search_operations(currency_transaction, search_bar=word_filter)
        if len(word_filter_transaction) == 0:
            print("Совпадений не найдено")
    else:
        word_filter_transaction = currency_transaction

    print("Программа: Распечатываю итоговый список транзакций...")

    count = len([word_filter_transaction])
    print(f"Программа:\n Всего банковских операций в выборке: {count}")

    for tr in word_filter_transaction:

        if "date" not in tr:
            print(f"Ошибка: транзакция не содержит ключ 'date': {tr}")
            return
        else:
            tr_data = get_date(tr.get("date"))

        tr_description = tr.get("description")

        if tr.get("description") == "Открытие вклада":
            from_to_tr = mask_account_card(tr.get("to"))
        else:
            from_to_tr = mask_account_card(tr.get("from")) + " " + "->" + " " + mask_account_card(tr.get("to"))
        amount_in_transaction = 0
        if start_menu == "1":
            amount_in_transaction = tr["operationAmount"]["amount"]
        elif start_menu == "2" or start_menu == "3":
            amount_in_transaction = tr["amount"]
        tr_amount_round = round(float(amount_in_transaction))
        tr_currency = 0
        if start_menu == "1":
            tr_currency = tr["operationAmount"]["currency"]["name"]
        elif start_menu == "2" or start_menu == "3":
            tr_currency = tr["currency_code"]
        print(
            f"""{tr_data} {tr_description}
{from_to_tr}
Сумма: {tr_amount_round} {tr_currency}.\n"""
        )


if __name__ == "__main__":
    main()
