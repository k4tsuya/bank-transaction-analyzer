"""Module for generating data from bank transactions."""

import pandas as pd
from .app import count_shop_visits, purchase_dates, shop_distance


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


def generate_purchase_data(
    shop_name: str,
) -> dict[str, list[dict[str, str]]]:
    """Generate and print a purchase report for a specific shop."""
    report_data = {shop_name: purchase_dates(shop_name)[shop_name]}

    df = pd.DataFrame(report_data[shop_name])

    with open(f"{shop_name.lower()}_purchase_report.txt", "w") as f:
        f.write("_" * 50 + "\n\n")
        f.write(f"{shop_name} Purchase Report\n")
        f.write("_" * 50 + "\n\n")
        f.write(f"{df.to_string(index=False, justify='right')}\n")

    return report_data
