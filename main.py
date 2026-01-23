"""Simple KM declaration script."""

from src.data_filter import (
    generate_declaration_data,
    filter_purchase_data,
    filter_date,
    filter_bank_number,
)
from src.app import load_bank_data, purchase_dates
from src.report_generation import (
    print_declaration_report,
    print_purchase_report,
)

if __name__ == "__main__":
    # print_declaration_report()
    # print_purchase_report("Sligro")
    # print(filter_date("2025-12-24"))

    print(filter_bank_number("936"))
