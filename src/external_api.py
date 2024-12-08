import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount(transact: dict) -> Any:
    """Функция, принимающая на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        amount = 0
        currency = transact["operationAmount"]["currency"]["code"]
        amount += float(transact["operationAmount"]["amount"])
        if currency == "RUB":

            return amount

        else:
            frm = transact["operationAmount"]["currency"]["code"]
            to = "RUB"
            url = f"https://api.apilayer.com/exchangerates_data/convert"
            payload = {"amount": transact["operationAmount"]["amount"], "from": frm, "to": to}
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers, data=payload)
            status_code = response.status_code
            print(status_code)

            if status_code == 200:
                result = response.json()
                convert = float(result["info"]["rate"])
                amount += convert
                return amount
            else:
                return f"Запрос не был успешным. Возможная причина: {response.reason}"

    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")


print(transaction_amount({'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}))
# 616804.608265
