from unittest.mock import patch

from src.reading_transactions import get_csv_transactions, get_excel_transactions


@patch("src.reading_transactions.pd.read_csv")
def test_get_csv_transaction(mock_read, test_csv_xlsx):
    mock_read.return_value = test_csv_xlsx
    result = get_csv_transactions("C:/Users/vikas/py_prj/homework/data/transactions.csv")
    expected = test_csv_xlsx.to_dict(orient="records")
    assert result == expected


def test_get_csv_transaction_incorrect_path() -> None:
    assert get_csv_transactions("") == []


@patch("src.reading_transactions.pd.read_excel")
def test_get_excel_transactions(mock_read, test_csv_xlsx):
    mock_read.return_value = test_csv_xlsx
    result = get_excel_transactions("C:/Users/vikas/py_prj/homework/data/transactions_excel.xlsx")
    expected = test_csv_xlsx.to_dict(orient="records")
    assert result == expected


def test_get_excel_transaction_incorrect_path() -> None:
    assert get_excel_transactions("") == []
