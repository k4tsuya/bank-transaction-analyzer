"""Simple KM declaration script."""

from src.app import load_bank_data, purchase_dates
from src.data_generation import (
    generate_purchase_data,
    generate_declaration_data,
)
from src.report_generation import print_declaration_report

if __name__ == "__main__":
    load_bank_data()
    generate_declaration_data()
    print_declaration_report()
