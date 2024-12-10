from typing import Union
import logging
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "logs", "masks.log", )

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=file_path,encoding='utf-8',
                    filemode='w')


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Функция маскировки номера банковской карты"""
    try:
        logging.info('Преобразуем полученное значение карты в строку')
        card_number_str = str(card_number)

        if card_number_str.isdigit() and len(card_number_str) == 16:
            logging.info('Маскируем строку с номером карты')
            return f'{card_number_str[-16:-12]} {card_number_str[-12:-10]}** **** {card_number_str[-4:]}'

        else:
            logging.info('Введены неверные данные')
            return 'Please enter a valid value'

    except Exception as ex:
        logging.error(f'Произошла ошибка {ex}', exc_info=True)


def get_mask_account(account_number: Union[str | int]) -> str:
    """Функция маскировки номера банковского счета"""
    try:
        logging.info('Преобразуем полученное значение счета в строку')
        account_number_str = str(account_number)

        if account_number_str.isdigit() and len(account_number_str) == 20:
            logging.info('Маскируем строку с номером счета')
            return f'**{account_number_str[-4:]}'

        else:
            logging.info('Введены неверные данные')
            return 'Please enter a valid value'

    except Exception as ex:
        logging.error(f'Произошла ошибка {ex}', exc_info=True)
