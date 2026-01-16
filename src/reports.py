"""Module for generating reports."""

import pandas as pd

from .app import count_shop_visits, shop_distance


def generate_report() -> None:
    """Generate and print a report."""
    report_data = {}

    report_data["Visit count"] = count_shop_visits()
    report_data["Distance"] = shop_distance()
    report_data["Subtotal km"] = {
        shop: report_data["Visit count"][shop] * report_data["Distance"][shop]
        for shop in report_data["Visit count"]
    }

    df = pd.DataFrame(report_data)

    total = {
        "Subtotal km": sum(report_data["Subtotal km"].values()),
    }

    print(df)
    print("------------------------------------------------")
    print("Total: ", total["Subtotal km"], "KM")
