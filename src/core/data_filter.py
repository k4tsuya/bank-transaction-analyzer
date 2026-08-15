"""Module for filtering data from bank transactions."""

import pandas as pd

from src.core.analyzer import (
    bank_data as _bank_data,
)
from src.core.analyzer import (
    count_shop_visits,
    purchase_dates,
    shop_distance,
)


def generate_declaration_data(month: str | None) -> pd.DataFrame:
    """
    Generate and print a report based on the provided month.

    Data is filtered by the provided month. If no month is provided, all data is considered.

    Args:
        month (str | None): The month to filter data by, in 'MM' format

    """
    report_data: dict[str, dict[str, int] | dict[str, float]] = {}

    report_data["Visit count"] = count_shop_visits(month)
    report_data["Distance"] = shop_distance()
    report_data["Subtotal km"] = {
        shop: report_data["Visit count"][shop] * report_data["Distance"][shop]
        for shop in report_data["Visit count"]
    }

    return pd.DataFrame(report_data)


def filter_purchase_data(
    shop_name: str,
) -> pd.DataFrame:
    """
    Generate and print a purchase report for a specific shop.

    Data is filtered by the provided shop name.

    Args:
        shop_name (str): The name of the shop to filter data by.
    """
    report_data = purchase_dates(shop_name)

    return pd.DataFrame(report_data[shop_name])


def filter_dates(
    start_date: str,
    end_date: str | None,
) -> pd.DataFrame:
    """
    Filter bank data for a specific date.

    Data is filtered by the provided start and end dates.
        If no end date is provided, only the start date is considered.

    Args:
        start_date (str): The start date for filtering transactions.
        end_date (str | None): The end date for filtering transactions.
            If None, only the start date is considered.
    """
    # Sets default value for end date.
    end_date = end_date if end_date else start_date

    FILTERED_DATA = "Purchase Data"

    data: dict[str, list] = {FILTERED_DATA: []}

    for item in _bank_data:
        date = item[4]
        counter_iban = item[8]
        counter_party = item[9]
        amount = item[6]
        description = item[19]
        if start_date <= date <= end_date:
            data[FILTERED_DATA].append(
                {
                    "Date": date,
                    "Counter Party": counter_party,
                    "Amount": amount,
                    "IBAN": counter_iban,
                    "Description": description,
                },
            )
    return pd.DataFrame(data[FILTERED_DATA])


def filter_bank_number(iban: str) -> pd.DataFrame:
    """
    Filter bank data for a specific IBAN number.

    Data is filtered by the provided IBAN number.

    Args:
        iban (str): The IBAN number to filter data by.

    """
    data: dict[str, list] = {iban: []}

    for item in _bank_data:
        counter_party_iban = item[8]
        date = item[4]
        counter_party = item[9]
        amount = item[6]
        description = item[19]
        if iban in counter_party_iban:
            data[iban].append(
                {
                    "IBAN": counter_party_iban,
                    "Date": date,
                    "Counter Party": counter_party,
                    "Amount": amount,
                    "Description": description,
                },
            )

    return pd.DataFrame(data[iban])


def filter_name(name: str) -> pd.DataFrame:
    """
    Filter bank data for a specific name.

    Data is filtered by the provided name.

    Args:
        name (str): The name to filter data by.
    """
    data: dict[str, list] = {name: []}

    for item in _bank_data:
        counter_party_name = item[9]
        date = item[4]
        iban = item[8]
        amount = item[6]
        description = item[19]
        if name.lower() in counter_party_name.lower():
            data[name].append(
                {
                    "IBAN": iban,
                    "Name": counter_party_name,
                    "Date": date,
                    "Amount": amount,
                    "Description": description,
                },
            )
    return pd.DataFrame(data[name])
