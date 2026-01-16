"""Module for generating reports."""

from .app import calculate_subtotal_km, count_store_visits, print_shop_visits


def generate_report() -> None:
    """Generate and print a report."""
    report: str = ""

    print("Generating report...\n")

    report += "Shop Visits:\n"
    count_store_visits()
    for item in count_store_visits():
        report += f"{item.title()}: {count_store_visits()[item]}\n"
    report += "\nKM Driven:\n\n"
    subtotals = calculate_subtotal_km()
    report += f"Hanos Km: {round(subtotals['hanos_km'])}\n"
    report += f"Sligro Km: {round(subtotals['sligro_km'])}\n"
    report += f"Makro Km: {round(subtotals['makro_km'])}\n"
    report += f"Horeca Plus Km: {round(subtotals['horeca_plus_km'])}\n"
    report += f"Eldee Km: {round(subtotals['eldee_km'])}\n"
    report += "----------------------\n"
    report += f"Total KM: {round(subtotals['total_km'])}\n"
    print(report)


generate_report()
