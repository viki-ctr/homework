import os
from src.utils import transaction
from src.reading_transactions import get_csv_transactions, get_excel_transactions
from src.processing import filter_by_state, sort_by_date, search_operations, count_categories


base_dir = os.path.dirname(os.path.abspath(__file__))
PATH_TO_FILE_JSON = os.path.join(base_dir, "..", "data", "operations.json")
PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def main():
    """Основная логика программы"""

    print('''Программа: Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
          ''')
    start_menu = input('Пользователь: ')

    #Получаем данные из файлов
    if start_menu == '1':
        print('Программа: Для обработки выбран JSON-файл.')
        transactions = transaction(PATH_TO_FILE_JSON)
    elif start_menu == '2':
        print('Программа: Для обработки выбран CSV-файл.')
        transactions = get_csv_transactions(PATH_TO_FILE_CSV)
    elif start_menu == '3':
        print('Программа: Для обработки выбран XLSX-файл.')
        transactions = get_excel_transactions(PATH_TO_FILE_EXCEL)
    else:
        print('Некорректный ввод')
        return

    print('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
           Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    operation_statues = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        try:
            user_statues = input('Пользователь: ').upper()
            statues_str = str(user_statues)
            if statues_str not in operation_statues:
                print('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
               Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
            else:
                break
        except Exception:
            print('введены некорретные данные')

    filtered_list = filter_by_state(transactions, state=user_statues)
    print(f'Программа: Операции отфильтрованы по статусу {user_statues}')

    sorted_operations = input('Программа: Отсортировать операции по дате? Да/Нет ')
    if sorted_operations.lower() == 'да':






if __name__ == "__main__":
    main()
