"""Module for filtering data from bank transactions."""

import pandas as pd

from .app import count_shop_visits, purchase_dates, shop_distance, bank_data


def generate_declaration_data() -> pd.DataFrame:
    """Generate and print a report."""
    report_data = {}

    report_data["Visit count"] = count_shop_visits()
    report_data["Distance"] = shop_distance()
    report_data["Subtotal km"] = {
        shop: report_data["Visit count"][shop] * report_data["Distance"][shop]
        for shop in report_data["Visit count"]
    }

    return pd.DataFrame(report_data)


def filter_purchase_data(
    shop_name: str,
) -> pd.DataFrame:
    """Generate and print a purchase report for a specific shop."""
    report_data = purchase_dates(shop_name)

    return pd.DataFrame(report_data[shop_name])


def filter_date(purchase_date: str) -> pd.DataFrame:
    """Filter bank data for a specific date."""
    data = {}

    for item in bank_data:
        date = item[4]
        counter_party = item[9]
        amount = item[6]
        description = item[19]
        if purchase_date == date:
            data[date] = {
                "Counter Party": counter_party,
                "Amount": amount,
                "Description": description,
            }

    return pd.DataFrame(data)
