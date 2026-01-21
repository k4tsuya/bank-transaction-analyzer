"""Module for generating reports."""

import pandas as pd

from .app import count_shop_visits, purchase_dates, shop_distance


def generate_report() -> str:
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

    data = ""

    with open("report.txt", "w") as f:
        f.write("_" * 50 + "\n\n")
        f.write("KM Declaration Report\n")
        f.write("_" * 50 + "\n\n")
        f.write(f"{df.to_string(justify='right')}\n")
        f.write("_" * 50 + "\n\n")
        f.write(f"Total KM: {total['Subtotal km']} KM\n")

    return data


def generate_purchase_report(
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
