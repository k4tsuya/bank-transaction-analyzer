import pytest

from src.core.analyzer import (
    count_shop_visits,
    load_bank_data,
    purchase_dates,
    shop_distance,
)


def test_load_bank_data():
    "Test that the bank data is loaded correctly."
    data = load_bank_data()
    assert data is not None


def test_count_shop_visits():
    "Test that valid month input returns a dictionary with integer counts."
    result = count_shop_visits("1")
    assert isinstance(result, dict)
    assert all(isinstance(count, int) for count in result.values())


def test_count_shop_visits_invalid_month():
    "Test that an invalid month raises a ValueError."
    with pytest.raises(ValueError):
        count_shop_visits("13")


def test_count_shop_visits_non_numeric_month():
    "Test that a non-numeric month raises a ValueError."
    with pytest.raises(ValueError):
        count_shop_visits("abc")


def test_shop_distance():
    "Test that the function returns a dictionary with expected keys and values."
    distances = shop_distance()
    assert distances["Hanos"] == 12
    assert distances["Sligro"] == 10
    assert set(distances) == {"Hanos", "Sligro", "Makro", "Horeca-Plus", "Eldee"}


def test_purchase_dates_invalid_shop():
    "Test that purchase_dates raises ValueError for an unknown shop."
    with pytest.raises(ValueError):
        purchase_dates("unknown")


def test_purchase_dates_existing_shop_returns_records():
    "Test that purchase_dates returns transaction details for a known shop."
    result = purchase_dates("Sligro")

    assert set(result) == {"Sligro"}
    records = result["Sligro"]
    assert records
    assert all(
        set(record) == {"Date", "Debit/Credit", "Transaction ID"} for record in records
    )
    assert all(isinstance(record["Date"], str) for record in records)
    assert all(isinstance(record["Debit/Credit"], str) for record in records)
    assert all(isinstance(record["Transaction ID"], str) for record in records)
